# 02 — Raspberry Pi 2 temporary Klipper host

The Raspberry Pi 2 is a temporary acceptance-test host only.

## Suggested system

- Raspberry Pi OS Lite, 32-bit build compatible with the specific Pi 2 revision
- SSH enabled
- wired Ethernet
- suggested hostname: `revival-bench`

## Base packages

```bash
sudo apt update
sudo apt full-upgrade -y
sudo apt install -y git can-utils dfu-util
```

## Install Klipper, Moonraker and Mainsail

KIAUH is a convenient installer for this disposable bench host:

```bash
cd ~
git clone https://github.com/dw-0/kiauh.git
~/kiauh/kiauh.sh
```

Install Klipper, Moonraker and Mainsail. KlipperScreen and Crowsnest are not required for this bench.

## Baseline checks

```bash
uname -a
cat /etc/os-release
lsusb
systemctl status klipper --no-pager
systemctl status moonraker --no-pager
```

## Evidence directory

```bash
mkdir -p ~/revival-evidence
```

Copy [snapshot.sh](scripts/snapshot.sh) to the Pi and run it after each significant phase.
