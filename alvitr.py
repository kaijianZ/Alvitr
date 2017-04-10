import getpids
import login
import saveimg
import threading

pids = getpids.getpids()
print('pids retrieved')

cookies = login.login()
print('cookies retrieved')

for slice in range(10):
    t = threading.Thread(target=saveimg.saveimg, args=(pids[slice * 5: slice * 5 + 5], cookies))
    t.start()
    # multi-thread
