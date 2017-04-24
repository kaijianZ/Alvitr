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

    pids, image_dir = alvitr.get_pids()
    print(len(pids), 'pids retrieved')

    cookies = login.login()
    print('cookies retrieved')

    slice_size = int(len(pids) / 10 + 0.5)

    for SLICE in range(10):
        t = threading.Thread(target=saveimg.saveimg,
                             args=(pids[SLICE * slice_size: SLICE * slice_size + slice_size], cookies, image_dir))
        t.start()
        # multi-thread
