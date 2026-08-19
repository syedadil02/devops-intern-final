#!/usr/bin/env bash
# ==============================================================================
# Description : Displays basic Linux system information (user, date, disk usage)
# Author      : Syed Adil
# ==============================================================================

set -euo pipefail

echo "=========================================="
echo "          SYSTEM INFORMATION              "
echo "=========================================="

echo -e "\n[1] Current User:"
whoami

echo -e "\n[2] Current Date & Time:"
date

echo -e "\n[3] Disk Usage (Human Readable):"
df -h

echo "=========================================="
echo "          END OF REPORT                   "
echo "=========================================="
