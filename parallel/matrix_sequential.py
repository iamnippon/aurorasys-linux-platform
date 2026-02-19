"""
AuroraSys Parallel Module
Sequential Matrix Multiplication

This script performs matrix multiplication using a single process.
It serves as the baseline for performance comparison against
the parallel implementation.
"""

import numpy as np
import time
from typing import Tuple


def generate_matrices(size: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate two random square matrices of given size.
    """
    np.random.seed(42)
    a = np.random.rand(size, size)
    b = np.random.rand(size, size)
    return a, b


def sequential_multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Perform matrix multiplication sequentially.
    """
    return np.dot(a, b)


def run_benchmark(size: int) -> float:
    """
    Generate matrices and measure execution time.
    Returns execution time in seconds.
    """
    a, b = generate_matrices(size)

    start_time = time.time()
    _ = sequential_multiply(a, b)
    end_time = time.time()

    return end_time - start_time


def main():
    MATRIX_SIZE = 800  # Adjust for performance testing

    print("=== Sequential Matrix Multiplication ===")
    print(f"Matrix size: {MATRIX_SIZE} x {MATRIX_SIZE}")
    print()

    execution_time = run_benchmark(MATRIX_SIZE)

    print(f"Execution Time: {execution_time:.4f} seconds")
    print("Benchmark complete.")


if __name__ == "__main__":
    main()
