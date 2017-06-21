import sys
import threading

import getpids
import login
import saveimg

if __name__ == "__main__":

    if len(sys.argv) == 1:
        alvitr = getpids.Daily()
    elif sys.argv[1] == "date":
        alvitr = getpids.Daily(date=sys.argv[2])
    elif sys.argv[1] == "tag":
        alvitr = getpids.Tag(tag=sys.argv[2])
    else:
        alvitr = getpids.Daily()
    # determine the download method by given argument

    while 1:
        id = input("id: ")
        password = input("password: ")

        loginSuccess, cookies = login.login(id, password)
        if loginSuccess:
            break
        elif len(id) == 0 and len(password) == 0:
            exit()
        else:
            print("Login failed. Please retry:")

    pids, image_dir = alvitr.get_pids()
    print(len(pids), 'pids retrieved')

    print('cookies retrieved')

    while len(pids):
        t = threading.Thread(target=saveimg.saveimg,
                             args=(pids[0:10], cookies, image_dir))
        pids = pids[10:]
        t.start()
        # multi-thread
