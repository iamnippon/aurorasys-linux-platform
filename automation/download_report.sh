#!/bin/bash

# =====================================================
# AuroraSys Automation Module
# Report Download & Archival Script
# =====================================================

set -euo pipefail

# Load environment variables
if [ -f "config.env" ]; then
    source config.env
else
    echo "[ERROR] config.env not found."
    exit 1
fi

# Validate required variables
if [[ -z "${DOWNLOAD_URL:-}" || -z "${REPORT_NAME:-}" || -z "${DESTINATION_DIR:-}" ]]; then
    echo "[ERROR] Required environment variables missing."
    exit 1
fi

# Create destination directory if it does not exist
mkdir -p "$DESTINATION_DIR"

# Create logs directory
LOG_DIR="logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/download_$(date +%Y%m%d_%H%M%S).log"

echo "[INFO] Starting download at $(date)" | tee -a "$LOG_FILE"

# Download file (prefer wget, fallback to curl)
if command -v wget >/dev/null 2>&1; then
    wget -O "$DESTINATION_DIR/$REPORT_NAME" "$DOWNLOAD_URL" >> "$LOG_FILE" 2>&1
elif command -v curl >/dev/null 2>&1; then
    curl -o "$DESTINATION_DIR/$REPORT_NAME" "$DOWNLOAD_URL" >> "$LOG_FILE" 2>&1
else
    echo "[ERROR] Neither wget nor curl is installed." | tee -a "$LOG_FILE"
    exit 1
fi

# Verify download
if [ -f "$DESTINATION_DIR/$REPORT_NAME" ]; then
    echo "[SUCCESS] Report downloaded to $DESTINATION_DIR/$REPORT_NAME" | tee -a "$LOG_FILE"
else
    echo "[ERROR] Download failed." | tee -a "$LOG_FILE"
    exit 1
fi

echo "[INFO] Completed at $(date)" | tee -a "$LOG_FILE"
exit 0
