MAXBLOCKS = 30
disk = [0] * MAXBLOCKS

def reset_disk():
    for i in range(MAXBLOCKS):
        disk[i] = 0

def contiguous_allocation():
    reset_disk()
    print("\n--- Contiguous Allocation ---")
    nf = int(input("Enter number of files: "))
    table = []
    for f in range(1, nf + 1):
        start, length = map(int, input(f"File {f} - starting block, length: ").split())
        if all(0 <= i < MAXBLOCKS and disk[i] == 0 for i in range(start, start + length)):
            for i in range(start, start + length):
                disk[i] = 1
            print(f"File {f} allocated blocks {start} to {start + length - 1}")
            table.append((f, start, length, f"{start}..{start + length - 1}"))
        else:
            print("Allocation failed: blocks not free/out of range.")
            table.append((f, start, length, "Failed"))
    print("\nFile\tStart\tLength\tBlocks")
    for row in table:
        print(f"F{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

def linked_allocation():
    reset_disk()
    print("\n--- Linked Allocation ---")
    nf = int(input("Enter number of files: "))
    table = []
    for f in range(1, nf + 1):
        length = int(input(f"File {f} - number of blocks: "))
        blocks = []
        for i in range(MAXBLOCKS):
            if len(blocks) == length:
                break
            if disk[i] == 0:
                disk[i] = 1
                blocks.append(i)
        chain = " -> ".join(map(str, blocks)) + " -> (NULL)" if blocks else "(NULL)"
        print(f"File {f} allocated blocks: {chain}")
        if len(blocks) < length:
            print("Warning: disk full, could not allocate all blocks.")
        table.append((f, chain))
    print("\nFile\tBlock Chain")
    for f, chain in table:
        print(f"F{f}\t{chain}")

def indexed_allocation():
    reset_disk()
    print("\n--- Indexed Allocation ---")
    nf = int(input("Enter number of files: "))
    table = []
    for f in range(1, nf + 1):
        length = int(input(f"File {f} - number of data blocks needed: "))
        index_block = -1
        for i in range(MAXBLOCKS):
            if disk[i] == 0:
                index_block = i
                disk[i] = 1
                break
        blocks = []
        if index_block != -1:
            for i in range(MAXBLOCKS):
                if len(blocks) == length:
                    break
                if disk[i] == 0:
                    disk[i] = 1
                    blocks.append(i)
        data_str = " ".join(map(str, blocks)) if blocks else "None"
        print(f"File {f} - Index block: {index_block}, Data blocks: {data_str}")
        if index_block == -1 or len(blocks) < length:
            print("Warning: disk full, could not allocate all blocks.")
        table.append((f, index_block, data_str))
    print("\nFile\tIndex Block\tData Blocks")
    for f, idx, data_str in table:
        print(f"F{f}\t{idx}\t\t{data_str}")

def main():
    print("Menu:\n1. Contiguous Allocation\n2. Linked Allocation\n3. Indexed Allocation")
    choice = int(input("Enter choice: "))
    if choice == 1:
        contiguous_allocation()
    elif choice == 2:
        linked_allocation()
    elif choice == 3:
        indexed_allocation()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()