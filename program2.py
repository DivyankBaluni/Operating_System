import threading

NUM_THREADS = 4

def sum_array(data, idx):
    start, end = data[idx]["start"], data[idx]["end"]
    data[idx]["sum"] = sum(range(start, end))
    print(f"Thread {threading.get_ident() % 100000}: sum[{start}..{end}) = {data[idx]['sum']}")

def main():
    n = 1_000_000
    chunk = n // NUM_THREADS
    data = []
    threads = []

    for i in range(NUM_THREADS):
        start = i * chunk
        end = n if i == NUM_THREADS - 1 else (i + 1) * chunk
        data.append({"start": start, "end": end, "sum": 0})

    for i in range(NUM_THREADS):
        t = threading.Thread(target=sum_array, args=(data, i))
        threads.append(t)
        t.start()

    total = 0
    for i in range(NUM_THREADS):
        threads[i].join()
        total += data[i]["sum"]

    print(f"Total sum (0 to {n - 1}) computed using {NUM_THREADS} threads = {total}")

if __name__ == "__main__":
    main()