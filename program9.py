def show_step(page, frames, hit):
    f_str = " ".join("-" if x == -1 else str(x) for x in frames)
    print(f"{page}\t{f_str}\t\t{'Hit' if hit else 'Fault'}")

def fifo(ref, nf):
    print("\n--- FIFO ---")
    print("Page\tFrames\t\tStatus")
    frames = [-1] * nf
    front = faults = 0
    for page in ref:
        if page in frames:
            show_step(page, frames, True)
        else:
            frames[front] = page
            front = (front + 1) % nf
            faults += 1
            show_step(page, frames, False)
    print(f"FIFO Page Faults = {faults}")

def lru(ref, nf):
    print("\n--- LRU ---")
    print("Page\tFrames\t\tStatus")
    frames = [-1] * nf
    last_used = [0] * nf
    filled = faults = 0
    for i, page in enumerate(ref):
        if page in frames:
            last_used[frames.index(page)] = i
            show_step(page, frames, True)
        else:
            faults += 1
            if filled < nf:
                idx = filled
                filled += 1
            else:
                idx = last_used.index(min(last_used))
            frames[idx] = page
            last_used[idx] = i
            show_step(page, frames, False)
    print(f"LRU Page Faults = {faults}")

def optimal(ref, nf):
    print("\n--- Optimal ---")
    print("Page\tFrames\t\tStatus")
    n = len(ref)
    frames = [-1] * nf
    filled = faults = 0
    for i, page in enumerate(ref):
        if page in frames[:filled]:
            show_step(page, frames, True)
            continue
        faults += 1
        if filled < nf:
            frames[filled] = page
            filled += 1
            show_step(page, frames, False)
            continue
        replace_idx, farthest = -1, -1
        for j in range(nf):
            k = i + 1
            while k < n and ref[k] != frames[j]:
                k += 1
            if k == n:
                replace_idx = j
                break
            if k > farthest:
                farthest, replace_idx = k, j
        frames[replace_idx] = page
        show_step(page, frames, False)
    print(f"Optimal Page Faults = {faults}")

def main():
    n = int(input("Enter number of pages in reference string: "))
    ref = list(map(int, input("Enter the reference string: ").split()))[:n]
    nf = int(input("Enter number of frames: "))
    fifo(ref, nf)
    lru(ref, nf)
    optimal(ref, nf)

if __name__ == "__main__":
    main()