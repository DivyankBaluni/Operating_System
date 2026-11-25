import threading
import time

mutex = threading.Semaphore(1)
wrt = threading.Semaphore(1)
read_count = 0
shared_data = 0

def reader(rid):
    global read_count
    mutex.acquire()
    read_count += 1
    if read_count == 1:
        wrt.acquire()
    mutex.release()
    print(f"Reader {rid}: read shared_data = {shared_data}")
    time.sleep(0.2)
    mutex.acquire()
    read_count -= 1
    if read_count == 0:
        wrt.release()
    mutex.release()

def writer(wid):
    global shared_data
    wrt.acquire()
    shared_data += 1
    print(f"Writer {wid}: wrote shared_data = {shared_data}")
    time.sleep(0.3)
    wrt.release()

if __name__ == "__main__":
    w1 = threading.Thread(target=writer, args=(1,))
    w1.start()
    readers = [threading.Thread(target=reader, args=(i,)) for i in range(1, 6)]
    for t in readers:
        t.start()
        
    w2 = threading.Thread(target=writer, args=(2,))
    w2.start()

    for t in readers:
        t.join()
    w1.join()
    w2.join()