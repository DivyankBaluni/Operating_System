P = 5
R = 3

available = [0] * R
maximum = [[0] * R for _ in range(P)]
allocation = [[0] * R for _ in range(P)]
need = [[0] * R for _ in range(P)]

def calculate_need():
    for i in range(P):
        for j in range(R):
            need[i][j] = maximum[i][j] - allocation[i][j]

def is_safe():
    work = available[:]
    finish = [False] * P
    safe_seq = []
    while len(safe_seq) < P:
        found = False
        for i in range(P):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(R)):
                for k in range(R):
                    work[k] += allocation[i][k]
                safe_seq.append(i)
                finish[i] = True
                found = True
        if not found:
            return False, []
    return True, safe_seq

def request_resources(pid, request):
    for j in range(R):
        if request[j] > need[pid][j]:
            print("Error: process has exceeded its maximum claim.")
            return False
        if request[j] > available[j]:
            print("Request denied: not enough resources available.")
            return False
    for j in range(R):
        available[j] -= request[j]
        allocation[pid][j] += request[j]
        need[pid][j] -= request[j]
    safe, seq = is_safe()
    if safe:
        print("Request can be granted safely.")
        print("New safe sequence:", " ".join(f"P{i}" for i in seq))
        return True
    for j in range(R):
        available[j] += request[j]
        allocation[pid][j] -= request[j]
        need[pid][j] += request[j]
    print("Request denied: would lead to an unsafe state.")
    return False

def main():
    global available
    available = list(map(int, input(f"Enter available resources ({R} types): ").split()))
    print(f"Enter Maximum matrix ({P} processes x {R} resources):")
    for i in range(P):
        maximum[i] = list(map(int, input(f"  P{i}: ").split()))
    print("Enter Allocation matrix:")
    for i in range(P):
        allocation[i] = list(map(int, input(f"  P{i}: ").split()))
    calculate_need()
    safe, seq = is_safe()
    if safe:
        print("System is in a SAFE state.")
        print("Safe sequence:", " ".join(f"P{i}" for i in seq))
    else:
        print("System is in an UNSAFE state.")
    pid = int(input("\nEnter process number requesting resources (0-4): "))
    request = list(map(int, input(f"Enter request vector ({R} values): ").split()))
    request_resources(pid, request)

if __name__ == "__main__":
    main()