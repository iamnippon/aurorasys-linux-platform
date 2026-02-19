#!/bin/bash

# =====================================================
# AuroraSys Security Module
# Unix Permission Demonstration Script
# =====================================================

set -euo pipefail

DEMO_DIR="permission_demo_workspace"
DEMO_FILE="example.txt"

echo "========================================"
echo "AuroraSys Permission Demonstration"
echo "Timestamp: $(date)"
echo "========================================"
echo ""

# 1️⃣ Create isolated workspace
mkdir -p "$DEMO_DIR"
cd "$DEMO_DIR"

# 2️⃣ Create sample file
echo "This is a sample file for permission testing." > "$DEMO_FILE"

echo "[INFO] Initial file permissions:"
ls -l "$DEMO_FILE"
echo ""

# 3️⃣ Remove all permissions
echo "[INFO] Removing all permissions (chmod 000)..."
chmod 000 "$DEMO_FILE"
ls -l "$DEMO_FILE"
echo ""

# 4️⃣ Apply read-only permission for owner
echo "[INFO] Setting owner read-only (chmod 400)..."
chmod 400 "$DEMO_FILE"
ls -l "$DEMO_FILE"
echo ""

# 5️⃣ Apply read-write for owner, read-only for group
echo "[INFO] Setting permissions to 640 (rw-r-----)..."
chmod 640 "$DEMO_FILE"
ls -l "$DEMO_FILE"
echo ""

# 6️⃣ Apply full permissions for owner
echo "[INFO] Setting permissions to 700 (rwx------)..."
chmod 700 "$DEMO_FILE"
ls -l "$DEMO_FILE"
echo ""

# 7️⃣ Demonstrate least privilege example
echo "[INFO] Applying least privilege (644 - rw-r--r--)..."
chmod 644 "$DEMO_FILE"
ls -l "$DEMO_FILE"
echo ""

echo "[INFO] Permission demonstration completed."
echo "Workspace located at: $(pwd)"
