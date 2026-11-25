def print_table(title, psize, allocation):
    print(f"\n--- {title} ---")
    print("Process No.\tProcess Size\tBlock No.")
    for i, size in enumerate(psize):
        where = f"B{allocation[i] + 1}" if allocation[i] != -1 else "Not Allocated"
        print(f"P{i + 1}\t\t{size}\t\t{where}")

def first_fit(bsize, psize):
    block = bsize[:]
    allocation = [-1] * len(psize)
    for i, size in enumerate(psize):
        for j in range(len(block)):
            if block[j] >= size:
                allocation[i] = j
                block[j] -= size
                break
    print_table("First Fit", psize, allocation)

def best_fit(bsize, psize):
    block = bsize[:]
    allocation = [-1] * len(psize)
    for i, size in enumerate(psize):
        best = -1
        for j in range(len(block)):
            if block[j] >= size and (best == -1 or block[j] < block[best]):
                best = j
        if best != -1:
            allocation[i] = best
            block[best] -= size
    print_table("Best Fit", psize, allocation)

def worst_fit(bsize, psize):
    block = bsize[:]
    allocation = [-1] * len(psize)
    for i, size in enumerate(psize):
        worst = -1
        for j in range(len(block)):
            if block[j] >= size and (worst == -1 or block[j] > block[worst]):
                worst = j
        if worst != -1:
            allocation[i] = worst
            block[worst] -= size
    print_table("Worst Fit", psize, allocation)

def main():
    bn = int(input("Enter number of memory blocks: "))
    bsize = list(map(int, input("Enter sizes of blocks: ").split()))[:bn]
    pn = int(input("Enter number of processes: "))
    psize = list(map(int, input("Enter sizes of processes: ").split()))[:pn]
    first_fit(bsize, psize)
    best_fit(bsize, psize)
    worst_fit(bsize, psize)

if __name__ == "__main__":
    main()