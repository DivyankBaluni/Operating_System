import multiprocessing
import os
import platform
import subprocess
import sys

def child_process():
    print(f"Child process: PID = {os.getpid()}, Parent PID = {os.getppid()}")
    cmd = ["cmd", "/c", "dir"] if platform.system() == "Windows" else ["ls", "-l"]
    print(f"Child is about to run '{' '.join(cmd)}'")
    result = subprocess.run(cmd)
    sys.exit(result.returncode)

def main():
    print(f"Parent process: PID = {os.getpid()}")
    child = multiprocessing.Process(target=child_process)
    child.start()
    print(f"Parent waiting for child (PID = {child.pid}) to finish...")
    child.join()
    print(f"Child exited with status {child.exitcode}")
    print("Parent process resumes and exits.")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()