"""
AuroraSys Concurrency Module
Deadlock Demonstration

This script demonstrates:
- Circular wait condition
- Resource locking
- Deadlock simulation
- Timeout-based detection

Two threads attempt to acquire two locks in opposite order,
creating a classic deadlock scenario.
"""

import threading
import time

# Two shared resources
lock_a = threading.Lock()
lock_b = threading.Lock()


def thread_one():
    print("[Thread 1] Attempting to acquire Lock A...")
    with lock_a:
        print("[Thread 1] Acquired Lock A.")
        time.sleep(1)

        print("[Thread 1] Attempting to acquire Lock B...")
        acquired = lock_b.acquire(timeout=3)

        if acquired:
            print("[Thread 1] Acquired Lock B.")
            lock_b.release()
        else:
            print("[Thread 1] Deadlock detected while waiting for Lock B.")

    print("[Thread 1] Released Lock A.")


def thread_two():
    print("[Thread 2] Attempting to acquire Lock B...")
    with lock_b:
        print("[Thread 2] Acquired Lock B.")
        time.sleep(1)

        print("[Thread 2] Attempting to acquire Lock A...")
        acquired = lock_a.acquire(timeout=3)

        if acquired:
            print("[Thread 2] Acquired Lock A.")
            lock_a.release()
        else:
            print("[Thread 2] Deadlock detected while waiting for Lock A.")

    print("[Thread 2] Released Lock B.")


def main():
    print("=== Deadlock Simulation ===\n")

    t1 = threading.Thread(target=thread_one)
    t2 = threading.Thread(target=thread_two)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nSimulation complete.")
    print("This demonstrates the circular wait condition in deadlock.")


if __name__ == "__main__":
    main()
