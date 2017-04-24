import getpids
import login
import saveimg
import threading
import sys


if __name__ == "__main__":

    if len(sys.argv) == 1:
        pixiv = getpids.Daily()
    elif sys.argv[1] == "date":
        pixiv = getpids.Daily(date=sys.argv[2])
    # elif sys.argv[1] == "tag":
    else:
        pixiv = getpids.Daily()
    pids, image_dir = pixiv.get_pids()
    print('pids retrieved')

    cookies = login.login()
    print('cookies retrieved')

    for slice in range(10):
        t = threading.Thread(target=saveimg.saveimg, args=(pids[slice * 5: slice * 5 + 5], cookies, image_dir))
        t.start()
        # multi-thread
