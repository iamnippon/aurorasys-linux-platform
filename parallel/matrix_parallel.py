"""
AuroraSys Parallel Module
Parallel Matrix Multiplication

This script performs matrix multiplication using multiprocessing.
The workload is divided by row chunks and distributed across CPU cores.
"""

import numpy as np
import time
import multiprocessing as mp
from typing import Tuple


def generate_matrices(size: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate two random square matrices of given size.
    """
    np.random.seed(42)
    a = np.random.rand(size, size)
    b = np.random.rand(size, size)
    return a, b


def multiply_chunk(args):
    """
    Multiply a chunk of matrix A with full matrix B.
    """
    a_chunk, b = args
    return np.dot(a_chunk, b)


def parallel_multiply(a: np.ndarray, b: np.ndarray, processes: int) -> np.ndarray:
    """
    Perform parallel matrix multiplication.
    """
    chunk_size = len(a) // processes
    chunks = []

    for i in range(processes):
        start = i * chunk_size
        end = None if i == processes - 1 else (i + 1) * chunk_size
        chunks.append((a[start:end], b))

    with mp.Pool(processes=processes) as pool:
        results = pool.map(multiply_chunk, chunks)

    return np.vstack(results)


def run_benchmark(size: int) -> float:
    """
    Generate matrices and measure parallel execution time.
    """
    a, b = generate_matrices(size)
    processes = mp.cpu_count()

    print(f"Using {processes} CPU cores.")

    start_time = time.time()
    _ = parallel_multiply(a, b, processes)
    end_time = time.time()

    return end_time - start_time


def main():
    MATRIX_SIZE = 800  # Adjust for performance testing

    print("=== Parallel Matrix Multiplication ===")
    print(f"Matrix size: {MATRIX_SIZE} x {MATRIX_SIZE}")
    print()

    execution_time = run_benchmark(MATRIX_SIZE)

    print(f"Execution Time: {execution_time:.4f} seconds")
    print("Benchmark complete.")


if __name__ == "__main__":
    mp.freeze_support()  # For Windows compatibility
    main()
