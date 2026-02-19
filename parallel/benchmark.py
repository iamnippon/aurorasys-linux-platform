"""
AuroraSys Parallel Module
Benchmark Comparison Script

Compares:
- Sequential matrix multiplication
- Parallel matrix multiplication

Outputs:
- Execution time comparison
- Speedup ratio
- CPU utilization snapshot
- Performance visualization
"""

import time
import numpy as np
import matplotlib.pyplot as plt
import psutil
import multiprocessing as mp

from matrix_sequential import sequential_multiply, generate_matrices
from matrix_parallel import parallel_multiply


MATRIX_SIZE = 800  # Adjust for your machine


def measure_sequential(a, b):
    start = time.time()
    sequential_multiply(a, b)
    end = time.time()
    return end - start


def measure_parallel(a, b):
    processes = mp.cpu_count()
    start = time.time()
    parallel_multiply(a, b, processes)
    end = time.time()
    return end - start


def main():
    print("=== AuroraSys Performance Benchmark ===")
    print(f"Matrix size: {MATRIX_SIZE} x {MATRIX_SIZE}")
    print()

    # Generate matrices once for fairness
    a, b = generate_matrices(MATRIX_SIZE)

    # CPU snapshot before test
    cpu_before = psutil.cpu_percent(interval=1)

    # Sequential benchmark
    print("Running sequential multiplication...")
    seq_time = measure_sequential(a, b)
    print(f"Sequential Time: {seq_time:.4f} seconds")

    # Parallel benchmark
    print("Running parallel multiplication...")
    par_time = measure_parallel(a, b)
    print(f"Parallel Time: {par_time:.4f} seconds")

    # CPU snapshot after test
    cpu_after = psutil.cpu_percent(interval=1)

    # Speedup calculation
    speedup = seq_time / par_time if par_time > 0 else 0

    print()
    print("=== Results ===")
    print(f"Speedup: {speedup:.2f}x")
    print(f"CPU Usage (before): {cpu_before}%")
    print(f"CPU Usage (after): {cpu_after}%")

    # Plot results
    labels = ["Sequential", "Parallel"]
    times = [seq_time, par_time]

    plt.figure()
    plt.bar(labels, times)
    plt.xlabel("Execution Mode")
    plt.ylabel("Time (seconds)")
    plt.title("Matrix Multiplication Performance Comparison")
    plt.tight_layout()

    output_file = "benchmark_result.png"
    plt.savefig(output_file)

    print(f"\nPerformance graph saved as {output_file}")
    print("Benchmark complete.")


if __name__ == "__main__":
    mp.freeze_support()
    main()
