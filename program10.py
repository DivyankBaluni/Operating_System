def fcfs(req, head):
    total, cur, seq = 0, head, [head]
    for r in req:
        total += abs(cur - r)
        cur = r
        seq.append(r)
    print("FCFS   total head movement =", total, "| Sequence:", " -> ".join(map(str, seq)))

def sstf(req, head):
    visited = [False] * len(req)
    total, cur, seq = 0, head, [head]
    for _ in range(len(req)):
        idx, best = -1, float("inf")
        for i, r in enumerate(req):
            if not visited[i] and abs(cur - r) < best:
                best, idx = abs(cur - r), i
        visited[idx] = True
        total += best
        cur = req[idx]
        seq.append(cur)
    print("SSTF   total head movement =", total, "| Sequence:", " -> ".join(map(str, seq)))

def scan(req, head, disk_size):
    arr = sorted(req + [head])
    idx = arr.index(head)
    total, cur, seq = 0, head, [head]
    for i in range(idx + 1, len(arr)):
        total += abs(cur - arr[i])
        cur = arr[i]
        seq.append(cur)
    total += abs(cur - (disk_size - 1))
    cur = disk_size - 1
    for i in range(idx - 1, -1, -1):
        total += abs(cur - arr[i])
        cur = arr[i]
        seq.append(cur)
    print("SCAN   total head movement =", total, "| Sequence:", " -> ".join(map(str, seq)))

def cscan(req, head, disk_size):
    arr = sorted(req + [head])
    idx = arr.index(head)
    total, cur, seq = 0, head, [head]
    for i in range(idx + 1, len(arr)):
        total += abs(cur - arr[i])
        cur = arr[i]
        seq.append(cur)
    total += abs(cur - (disk_size - 1))
    total += disk_size - 1
    cur = 0
    for i in range(idx):
        total += abs(cur - arr[i])
        cur = arr[i]
        seq.append(cur)
    print("C-SCAN total head movement =", total, "| Sequence:", " -> ".join(map(str, seq)))

def main():
    n = int(input("Enter number of requests: "))
    req = list(map(int, input("Enter the requests: ").split()))[:n]
    head = int(input("Enter initial head position: "))
    disk_size = int(input("Enter disk size (max cylinder + 1): "))
    fcfs(req, head)
    sstf(req, head)
    scan(req, head, disk_size)
    cscan(req, head, disk_size)

if __name__ == "__main__":
    main()