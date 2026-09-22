#!/usr/bin/env bash
set -euo pipefail
ip -details -statistics link show can0
"${HOME}/klippy-env/bin/python" "${HOME}/klipper/scripts/canbus_query.py" can0
