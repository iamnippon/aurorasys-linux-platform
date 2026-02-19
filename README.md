

# AuroraSys

**A Modular Linux-Based Enterprise Systems Simulation Platform**

---

## 🔍 Overview

AuroraSys is a modular Unix/Linux-based systems engineering project that simulates core components of an enterprise computing environment.

The platform integrates:

* Automation pipelines (Bash scripting)
* Concurrency and process management simulations
* Distributed communication using RPC
* Networking diagnostics tools
* File system and permission management
* Parallel computing benchmarks
* Security configuration demonstrations

This project demonstrates practical implementation of operating system principles in a structured, modular architecture.

---

## 🏗 System Architecture

```
                +----------------------+
                |    Automation Layer  |
                |  (Bash + Cron Jobs)  |
                +----------------------+
                          |
                          v
+----------------+  +------------------+  +-------------------+
| Concurrency    |  | RPC Distributed  |  | Networking Tools  |
| Simulation     |  | Service Module   |  | (ping, netstat)   |
+----------------+  +------------------+  +-------------------+
                          |
                          v
                +----------------------+
                |   Security & Access  |
                |   Control Module     |
                +----------------------+
                          |
                          v
                +----------------------+
                | Parallel Benchmark   |
                | Performance Analysis |
                +----------------------+
```

---

## 🧩 Modules

### 1️⃣ Automation Engine

Implements automated data retrieval and file organization using Bash scripts.

Features:

* Scheduled report downloads
* Logging system
* Error handling
* Cron integration

Technologies:

* Bash
* wget / curl
* Linux cron

---

### 2️⃣ Concurrency Simulation

Demonstrates multithreading and process scheduling behavior.

Features:

* Blocking vs non-blocking tasks
* Thread synchronization examples
* Deadlock simulation

Technologies:

* Python threading / multiprocessing

---

### 3️⃣ RPC Distributed Service

Implements a simple client-server architecture using RPC concepts.

Features:

* Client-server communication
* Parameter marshaling
* Network-based procedure execution

Technologies:

* Python socket RPC (or C rpcgen if implemented)

---

### 4️⃣ Networking Toolkit

Provides system-level network diagnostics.

Includes:

* Interface configuration checks
* Connectivity testing
* Port monitoring

Tools:

* ip addr
* ping
* netstat
* traceroute

---

### 5️⃣ File System & Permissions Lab

Demonstrates Unix permission models and access control.

Includes:

* rwx permission experiments
* ACL examples
* Least privilege demonstrations

---

### 6️⃣ Parallel Computing Benchmark

Evaluates performance difference between sequential and parallel execution.

Includes:

* Matrix multiplication benchmark
* Multiprocessing comparison
* Performance timing results

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/aurorasys.git
cd aurorasys
```

Ensure dependencies are installed:

```bash
sudo apt install wget curl net-tools
```

Python 3.10+ required.

---

## ▶️ Running Modules

Example: Run automation script

```bash
bash automation/download_report.sh
```

Example: Run concurrency demo

```bash
python3 concurrency/scheduler_demo.py
```

Example: Run parallel benchmark

```bash
python3 parallel/benchmark.py
```

---

## 📊 Example Output

```
[INFO] Download successful.
[INFO] File archived in /sales_reports/
```

```
Sequential Execution Time: 2.43 seconds
Parallel Execution Time: 0.91 seconds
Speedup: 2.67x
```

---

## 🔐 Security Considerations

* Demonstrates SSH vs Telnet security comparison
* Implements principle of least privilege
* Includes file permission hardening examples

---

## 🧠 Concepts Demonstrated

* Process scheduling
* Concurrency vs parallelism
* RPC communication model
* Unix file system structure
* Network interface configuration
* Automation in Linux environments
* Performance benchmarking

---

## 📈 Future Improvements

* Add Docker containerization
* Convert RPC module to gRPC
* Add REST API layer
* Implement real monitoring dashboard

---

## 📚 References

Operating Systems: Three Easy Pieces
Linux Command Line – Shotts
Remote Procedure Call – GeeksforGeeks

---

## 👤 Author

Nippon Chowdhury
BSc Computer Science
Systems & Distributed Computing Enthusiast

