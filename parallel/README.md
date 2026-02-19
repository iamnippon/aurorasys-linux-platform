

# Parallel Module

**Sequential vs Multi-Core Matrix Multiplication Benchmark**

---

## 1. Overview

The Parallel module evaluates the performance difference between single-process and multi-process computation using matrix multiplication as a CPU-bound workload.

It demonstrates:

* Baseline sequential execution
* Multi-core parallel execution
* Workload partitioning
* Speedup measurement
* CPU utilization observation
* Performance visualization

This module models how operating systems leverage multiple CPU cores to improve computational throughput.

---

## 2. Architecture

```
matrix_sequential.py
        ↓
Single-process NumPy multiplication
        ↓
Execution Time Measurement
```

```
matrix_parallel.py
        ↓
Row-wise workload partitioning
        ↓
Multiprocessing Pool
        ↓
Multi-core execution
```

```
benchmark.py
        ↓
Runs both implementations
        ↓
Calculates speedup
        ↓
Generates performance graph
```

---

## 3. Implemented Components

### 3.1 Sequential Implementation

`matrix_sequential.py`

* Uses NumPy `dot()`
* Executes in a single process
* Serves as baseline measurement

---

### 3.2 Parallel Implementation

`matrix_parallel.py`

* Detects available CPU cores
* Splits matrix rows into chunks
* Uses `multiprocessing.Pool`
* Executes chunk multiplication concurrently
* Reconstructs final result

---

### 3.3 Benchmark Script

`benchmark.py`

* Generates matrices once (fair comparison)
* Measures execution times
* Calculates speedup ratio
* Captures CPU utilization snapshot
* Generates performance graph (`benchmark_result.png`)

---

## 4. Concepts Demonstrated

* CPU-bound workload scaling
* Process-based parallelism
* Workload partitioning strategies
* Core utilization
* Performance benchmarking methodology
* Speedup calculation

Speedup formula:

```
Speedup = Sequential Time / Parallel Time
```

---

## 5. Requirements

Defined in `requirements.txt`:

```
numpy
matplotlib
psutil
```

Install dependencies:

```bash
pip install -r ../requirements.txt
```

Python 3.10+ required.

---

## 6. Usage

Run full benchmark:

```bash
python3 benchmark.py
```

Example output:

```
=== AuroraSys Performance Benchmark ===
Matrix size: 800 x 800

Sequential Time: 2.41 seconds
Parallel Time: 0.84 seconds

Speedup: 2.87x
Performance graph saved as benchmark_result.png
```

---

## 7. Performance Observations

* Parallel execution reduces computation time.
* Speedup depends on:

  * Number of CPU cores
  * System load
  * Memory bandwidth
* Overhead from process spawning affects small workloads.

This reflects real-world parallel computing trade-offs.

---

## 8. Practical Relevance

Parallel computation is fundamental in:

* Scientific computing
* Machine learning training
* Data processing pipelines
* Simulation systems
* High-performance computing (HPC)

This module models how operating systems distribute computational tasks across multiple cores.

---

## 9. Extension Opportunities

Possible enhancements:

* Dynamic matrix size via CLI argument
* Scaling analysis across multiple matrix sizes
* Core-by-core performance comparison
* Memory profiling
* Amdahl’s Law analysis

---

# Summary

The Parallel module demonstrates measurable computational acceleration through multi-core processing.

It provides a structured benchmarking workflow that highlights how operating systems enable scalable performance through multiprocessing.

