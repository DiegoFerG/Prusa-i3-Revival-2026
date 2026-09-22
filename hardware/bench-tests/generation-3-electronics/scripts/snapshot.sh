#!/usr/bin/env bash
set -u
OUTDIR="${HOME}/revival-evidence"
mkdir -p "$OUTDIR"
TS="$(date +%Y%m%d-%H%M%S)"
OUT="$OUTDIR/snapshot-$TS.txt"
{
  echo "=== REVIVAL GEN3 BENCH SNAPSHOT ==="
  date -Is
  echo "=== UNAME ==="; uname -a
  echo "=== OS ==="; cat /etc/os-release 2>/dev/null || true
  echo "=== USB ==="; lsusb 2>&1 || true
  echo "=== SERIAL BY-ID ==="; ls -l /dev/serial/by-id/ 2>&1 || true
  echo "=== NETWORK ==="; ip addr 2>&1 || true
  echo "=== CAN0 ==="; ip -details -statistics link show can0 2>&1 || true
  echo "=== KLIPPER ==="; systemctl status klipper --no-pager 2>&1 || true
  echo "=== MOONRAKER ==="; systemctl status moonraker --no-pager 2>&1 || true
  echo "=== RECENT KERNEL ==="; dmesg -T 2>&1 | tail -200 || true
} > "$OUT"
echo "Evidence written to: $OUT"
