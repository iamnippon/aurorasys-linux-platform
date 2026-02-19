#!/bin/bash

# =====================================================
# AuroraSys Networking Module
# Network Diagnostics Script
# =====================================================

set -euo pipefail

LOG_DIR="logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/network_check_$(date +%Y%m%d_%H%M%S).log"

echo "========================================" | tee -a "$LOG_FILE"
echo "AuroraSys Network Diagnostics" | tee -a "$LOG_FILE"
echo "Timestamp: $(date)" | tee -a "$LOG_FILE"
echo "========================================" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# 1️⃣ Display IP configuration
echo "[INFO] Network Interfaces:" | tee -a "$LOG_FILE"
ip addr | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# 2️⃣ Default gateway
echo "[INFO] Default Route:" | tee -a "$LOG_FILE"
ip route | grep default | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# 3️⃣ Connectivity test
TARGET="8.8.8.8"

echo "[INFO] Connectivity Test (Ping $TARGET):" | tee -a "$LOG_FILE"

if ping -c 3 "$TARGET" > /dev/null 2>&1; then
    echo "[SUCCESS] Internet connectivity verified." | tee -a "$LOG_FILE"
else
    echo "[ERROR] Unable to reach $TARGET." | tee -a "$LOG_FILE"
fi

echo "" | tee -a "$LOG_FILE"

# 4️⃣ DNS resolution test
DOMAIN="google.com"

echo "[INFO] DNS Resolution Test ($DOMAIN):" | tee -a "$LOG_FILE"

if getent hosts "$DOMAIN" > /dev/null 2>&1; then
    echo "[SUCCESS] DNS resolution working." | tee -a "$LOG_FILE"
else
    echo "[ERROR] DNS resolution failed." | tee -a "$LOG_FILE"
fi

echo "" | tee -a "$LOG_FILE"

# 5️⃣ Open listening ports
echo "[INFO] Active Listening Ports:" | tee -a "$LOG_FILE"

if command -v ss >/dev/null 2>&1; then
    ss -tuln | tee -a "$LOG_FILE"
elif command -v netstat >/dev/null 2>&1; then
    netstat -tuln | tee -a "$LOG_FILE"
else
    echo "[WARNING] Neither ss nor netstat is available." | tee -a "$LOG_FILE"
fi

echo "" | tee -a "$LOG_FILE"

echo "[INFO] Network diagnostics completed." | tee -a "$LOG_FILE"
echo "Log saved to: $LOG_FILE"
