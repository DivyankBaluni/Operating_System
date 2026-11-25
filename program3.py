from collections import deque

def print_result(p, title):
    n = len(p)
    print(f"\n--- {title} ---")
    print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")
    for x in p:
        print(f"{x['pid']}\t{x['at']}\t{x['bt']}\t{x['pr']}\t{x['ct']}\t{x['tat']}\t{x['wt']}")
    print(f"Average Waiting Time    = {sum(x['wt'] for x in p) / n:.2f}")
    print(f"Average Turnaround Time = {sum(x['tat'] for x in p) / n:.2f}")

def finish(x, time):
    x["ct"] = time
    x["tat"] = x["ct"] - x["at"]
    x["wt"] = x["tat"] - x["bt"]

def fcfs(processes):
    p = sorted([dict(x) for x in processes], key=lambda x: (x["at"], x["pid"]))
    time = 0
    for x in p:
        if time < x["at"]:
            time = x["at"]
        time += x["bt"]
        finish(x, time)
    print_result(sorted(p, key=lambda x: x["pid"]), "FCFS")

def sjf(processes):
    p = [dict(x) for x in processes]
    n = len(p)
    done = [False] * n
    completed = time = 0
    while completed < n:
        idx, min_bt = -1, float("inf")
        for i in range(n):
            if not done[i] and p[i]["at"] <= time and p[i]["bt"] < min_bt:
                min_bt, idx = p[i]["bt"], i
        if idx == -1:
            time += 1
            continue
        time += p[idx]["bt"]
        finish(p[idx], time)
        done[idx] = True
        completed += 1
    print_result(p, "SJF (Non-preemptive)")

def priority_scheduling(processes):
    p = [dict(x) for x in processes]
    n = len(p)
    done = [False] * n
    completed = time = 0
    while completed < n:
        idx, best = -1, float("inf")
        for i in range(n):
            if not done[i] and p[i]["at"] <= time and p[i]["pr"] < best:
                best, idx = p[i]["pr"], i
        if idx == -1:
            time += 1
            continue
        time += p[idx]["bt"]
        finish(p[idx], time)
        done[idx] = True
        completed += 1
    print_result(p, "Priority (Non-preemptive)")

def round_robin(processes, quantum):
    p = [dict(x) for x in processes]
    n = len(p)
    time = completed = 0
    in_queue = [False] * n
    queue = deque()
    for i in range(n):
        if p[i]["at"] <= time:
            queue.append(i)
            in_queue[i] = True
    while completed < n:
        if not queue:
            time += 1
            for i in range(n):
                if not in_queue[i] and p[i]["rem"] > 0 and p[i]["at"] <= time:
                    queue.append(i)
                    in_queue[i] = True
            continue
        idx = queue.popleft()
        sl = min(p[idx]["rem"], quantum)
        time += sl
        p[idx]["rem"] -= sl
        for i in range(n):
            if not in_queue[i] and p[i]["rem"] > 0 and p[i]["at"] <= time and i != idx:
                queue.append(i)
                in_queue[i] = True
        if p[idx]["rem"] > 0:
            queue.append(idx)
        else:
            finish(p[idx], time)
            completed += 1
            in_queue[idx] = False
    print_result(p, f"Round Robin (Quantum = {quantum})")

def main():
    n = int(input("Enter number of processes: "))
    p = []
    for i in range(n):
        at, bt, pr = map(int, input(f"Process {i + 1} - Arrival Time, Burst Time, Priority: ").split())
        p.append({"pid": i + 1, "at": at, "bt": bt, "pr": pr, "ct": 0, "tat": 0, "wt": 0, "rem": bt})
    print("\nMenu:\n1. FCFS\n2. SJF (Non-preemptive)\n3. Priority (Non-preemptive)\n4. Round Robin\n5. Compare All")
    choice = int(input("Enter choice: "))
    if choice == 1:
        fcfs(p)
    elif choice == 2:
        sjf(p)
    elif choice == 3:
        priority_scheduling(p)
    elif choice == 4:
        round_robin(p, int(input("Enter time quantum: ")))
    elif choice == 5:
        q = int(input("Enter time quantum for Round Robin: "))
        fcfs(p)
        sjf(p)
        priority_scheduling(p)
        round_robin(p, q)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()