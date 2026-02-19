"""
AuroraSys Concurrency Module
Threading Demonstration

This script demonstrates:
- Concurrent thread execution
- Shared resource synchronization
- Lock-based race condition prevention
- Execution time comparison
"""

import threading
import time
from typing import List

# Shared resource
shared_counter = 0

# Lock for synchronization
counter_lock = threading.Lock()

# Configuration
NUM_THREADS = 5
INCREMENTS_PER_THREAD = 100000


def unsafe_increment():
    """
    Increment shared_counter without synchronization.
    Demonstrates potential race condition.
    """
    global shared_counter
    for _ in range(INCREMENTS_PER_THREAD):
        shared_counter += 1


def safe_increment():
    """
    Increment shared_counter with lock protection.
    Prevents race condition.
    """
    global shared_counter
    for _ in range(INCREMENTS_PER_THREAD):
        with counter_lock:
            shared_counter += 1


def run_threads(target_function) -> float:
    """
    Runs multiple threads using the specified target function.
    Returns execution time.
    """
    threads: List[threading.Thread] = []
    start_time = time.time()

    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=target_function)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    return end_time - start_time


def main():
    global shared_counter

    print("=== Threading Demonstration ===")
    print(f"Threads: {NUM_THREADS}")
    print(f"Increments per thread: {INCREMENTS_PER_THREAD}")
    print()

    # Unsafe run
    shared_counter = 0
    print("Running without synchronization...")
    unsafe_time = run_threads(unsafe_increment)
    print(f"Final counter value (unsafe): {shared_counter}")
    print(f"Execution time: {unsafe_time:.4f} seconds")
    print()

    # Safe run
    shared_counter = 0
    print("Running with lock synchronization...")
    safe_time = run_threads(safe_increment)
    print(f"Final counter value (safe): {shared_counter}")
    print(f"Execution time: {safe_time:.4f} seconds")
    print()

    print("Expected counter value:", NUM_THREADS * INCREMENTS_PER_THREAD)
    print()
    print("Demonstration complete.")


if __name__ == "__main__":
    main()
