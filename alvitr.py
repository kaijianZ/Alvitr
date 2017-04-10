import getpids
import login
import saveimg
import threading

pids = getpids.getpids()
cookies = login.login()

for i in range(10):
    # multi-thread
    t = threading.Thread(target=saveimg.saveimg, args=(pids[i * 5: i * 5 + 5], cookies))
    t.start()
