import psutil

pids=psutil.pids()

for pid in pids:
    p=psutil.Process(pid)
    print(str(pid) +" = "+ p.name())
