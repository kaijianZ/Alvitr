import getpids
import login
import saveimg
import threading

pids = getpids.getpids()
cookies = login.login()

for slice in range(10):
    t = threading.Thread(target=saveimg.saveimg, args=(pids[slice * 5: slice * 5 + 5], cookies))
    t.start()
    # multi-thread
