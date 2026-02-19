
# Automation Module

**Report Retrieval & Archival Engine**

---

## 1. Overview

The Automation module implements a production-style Linux data retrieval pipeline using Bash scripting.

It demonstrates:

* Environment-based configuration
* Controlled file downloads
* Error handling
* Structured logging
* Directory management

This module simulates a scheduled enterprise report ingestion system.

---

## 2. Architecture

```
config.env
     ↓
download_report.sh
     ↓
Destination Directory
     ↓
Timestamped Log File
```

The script retrieves a remote file and archives it locally while maintaining execution logs.

---

## 3. Features

* Configuration-driven execution
* Automatic directory creation
* Timestamped logging
* wget → curl fallback mechanism
* Exit codes for automation workflows
* Safe scripting practices (`set -euo pipefail`)

---

## 4. Requirements

* Linux or macOS environment
* Bash shell
* wget or curl installed

---

## 5. Configuration

Copy the example configuration:

```bash
cp config.env.example config.env
```

Edit `config.env`:

```
DOWNLOAD_URL="https://example.com/report.csv"
REPORT_NAME="daily_sales_report.csv"
DESTINATION_DIR="$HOME/sales_reports"
```

Do not commit `config.env` to version control.

---

## 6. Usage

Make the script executable:

```bash
chmod +x download_report.sh
```

Run:

```bash
./download_report.sh
```

---

## 7. Output

Successful execution:

```
[INFO] Starting download...
[SUCCESS] Report downloaded to /home/user/sales_reports/daily_sales_report.csv
[INFO] Completed.
```

Log files are stored in:

```
automation/logs/
```

Each log file includes a timestamp for traceability.

---

## 8. Exit Codes

| Code | Meaning                           |
| ---- | --------------------------------- |
| 0    | Success                           |
| 1    | Configuration or download failure |

These exit codes allow integration into cron jobs or CI pipelines.

---

## 9. Cron Integration (Optional)

To schedule execution:

```bash
crontab -e
```

Example daily execution at 2 AM:

```
0 2 * * * /path/to/aurorasys/automation/download_report.sh
```

---

## 10. Security Considerations

* Configuration values stored in `.env`
* No hardcoded URLs
* No credentials committed to repository
* Logs stored locally

---

## 11. Practical Use Case

This module models real-world automation workflows such as:

* Nightly financial report downloads
* ETL staging pipelines
* Backup synchronization tasks
* Log archival systems

---
