# 2026-10-08 — CB1, Manta, EBB36 Gen2, Eddy Duo and camera USB bench

## Scope and evidence

Operator-reported terminal output, Mainsail console results and a dashboard screenshot from 8 October 2026 (Europe/Madrid). This records a separate Generation 3 bench, not commissioning of the printer or closure of original mechanical reassembly. CB1 is the current temporary host; CB2 remains the final target. The previous faulty Manta was returned; the current replacement is used. No motor, heater, EBB accelerometer or final CAN acceptance is claimed.

## Sequential benches and gates

| Bench | State at session close | Next gate |
|---|---|---|
| USB, Eddy directly on Manta | Four MCUs configured; LDC drive-current calibration and 30-minute raw capture completed | Keep as comparison baseline |
| USB, Eddy via EBB expansion | Enumeration and LDC communication passed after correcting data-wire order; camera video and reboot/cold start worked | 30-minute capture with camera streaming; compare baseline and inspect new USB/Klipper errors |
| Direct CAN, without CEB | Not started | Record exact firmware/build settings, mode selectors, power, endpoints/termination and UUIDs before migration; retain USB rollback |
| CAN through CEB | Not started; CEB still to order | Build and test only after direct CAN passes and CEB is received |
| Eddy distance/height calibration | Not performed | Print 3/5/10 mm spacers; fixed metal target and repeatable geometry; final mounted calibration later |

## As-tested connections

| Origin | Destination | Cable / connector / role |
|---|---|---|
| 24 V bench PSU | Manta VIN | Existing DC supply wiring; exact gauge/PSU measurements not recorded today |
| CB1 module sockets | Manta | CB1 mounted on Manta; internal host USB connection to Manta MCU |
| Manta host USB | EBB USB Adapter USB-C | USB data cable |
| 24 V bench PSU | EBB USB Adapter power input | Separate DC feed; USB host does not supply EBB main power |
| EBB USB Adapter | EBB36 Gen2 | Supplied MX3.0-to-XT30 harness |
| EBB USB/CAN expansion | Eddy Duo | Supplied short four-wire cable, Dupont end replaced with compatible four-pin crimp housing |
| Manta remaining host USB | Innomaker U30CAM-4K-S1 | Camera USB data/power cable; enumerated at USB 2.0 high speed |

In USB mode the EBB communication-selection jumper is open and the Eddy selector is at USB. Make connector/jumper changes only with all power removed. Exact final CAN termination positions are not validated by this USB bench.

### Important cable correction — USB only

Reference: at the EBB expansion header shown in the session, start at the pin nearest the large silver electrolytic capacitor and proceed away from it.

| Position | Validated short-cable colour |
|---|---|
| Nearest capacitor | Red |
| Second | Green |
| Third | Yellow |
| Farthest capacitor | Black |

Initial red–yellow–green–black wiring powered the Eddy LED but did not enumerate it. Swapping only yellow and green restored enumeration immediately; LDC calibration then succeeded. The initial assistant colour assignment was incorrect. Preserve red/black power positions. This is an empirical colour mapping for this delivered cable and USB mode, not a universal pinout or a validated CAN colour mapping. No multimeter was available; electrical continuity and voltages were not measured.

A closely matching user report is retained as context, not manufacturer sign-off: [BIQU forum, EBB gen2 with Eddy duo](https://community.biqu3d.com/topic/5203-ebb-gen2-with-eddy-duo/), USB success with red–green–yellow–black and another report of powered LED/no enumeration. Manufacturer reference: [EBB36 Gen2 wiki](https://global.bttwiki.com/EBB36_GEN2.html). Do not infer that an official schematic is wrong solely from a colour-order report.

## Firmware and persistent identities

| MCU | Observed firmware | Persistent connection |
|---|---|---|
| Manta STM32H723 | v0.11.0-267-g01ed8096 | /dev/serial/by-id/usb-Klipper_stm32h723xx_1A002F000A51333231343036-if00 |
| EBB STM32G0B1 | v0.13.0-146-g14cbb8dd2 | /dev/serial/by-id/usb-Klipper_stm32g0b1xx_EBB36_GEN-if00 |
| Eddy RP2040 | v0.13.0-786-g461c4e37 | /dev/serial/by-id/usb-Klipper_rp2040_5044340408A5361C-if00 |
| CB1 Linux MCU | v0.13.0-636-g293e1e9d | /tmp/klipper_host_mcu |

Host Klipper: v0.13.0-786-g461c4e37. CB1 image reports BIGTREETECH-CB1 3.1.0-26.05.0-trunk, Debian trixie, Linux 7.0.2-vendor-sunxi64. MCU versions differ; this is an observed snapshot, not a recommended version combination. ttyACM numbers changed during reconnects; persistent by-id paths did not.

The Eddy initially did not enumerate normally. BOOT-assisted USB connection exposed RP2 Boot (2e8a:0003). Its RP2040 USB build produced out/klipper.uf2 and was flashed successfully:

```bash
sudo systemctl stop klipper
cd ~/klipper
[ ! -f .config ] || cp .config .config.bak-antes-eddy-usb
make menuconfig
make clean
make
make flash FLASH_DEVICE=2e8a:0003
```

Observed build options include RP2040 and CONFIG_RP2040_FLASH_GENERIC_03=y; USB serial support was compiled. The complete .config was not uploaded, so do not treat this as a complete reproducible build-settings archive.

### Reported bench configuration excerpt

This is the known excerpt, not a download of the complete live printer.cfg. Keep kinematics:none; no homing or motion/height-calibration command is authorized by this excerpt.

```ini
[mcu]
serial: /dev/serial/by-id/usb-Klipper_stm32h723xx_1A002F000A51333231343036-if00

[mcu CB1]
serial: /tmp/klipper_host_mcu

[mcu EBB]
serial: /dev/serial/by-id/usb-Klipper_stm32g0b1xx_EBB36_GEN-if00

[mcu eddy]
serial: /dev/serial/by-id/usb-Klipper_rp2040_5044340408A5361C-if00

[printer]
kinematics: none
max_velocity: 1
max_accel: 1

[temperature_sensor eddy_mcu]
sensor_type: temperature_mcu
sensor_mcu: eddy
min_temp: 0
max_temp: 100

[probe_eddy_current btt_eddy]
sensor_type: ldc1612
i2c_mcu: eddy
i2c_bus: i2c0f
x_offset: 0
y_offset: 0
descend_z: 2.5

# Reported existing SAVE_CONFIG data:
#*# [probe_eddy_current btt_eddy]
#*# reg_drive_current = 16
```

The local probe implementation accepts descend_z and deprecates z_offset. Zero X/Y offsets are bench placeholders. descend_z is not measured sensor mounting geometry or a completed distance calibration. Initial CRC-mismatch/reset output was followed by successful communication; it did not establish hardware failure.

## Eddy measurements

LDC_CALIBRATE_DRIVE_CURRENT CHIP=btt_eddy returned 15 initially, then 16 repeatedly; 16 was saved. Through the corrected short cable it again returned 16 at 20:37. No further SAVE_CONFIG was required.

Direct-USB raw frequency capture, using ldc1612/dump_ldc1612 with sensor btt_eddy through ~/printer_data/comms/klippy.sock:

| Metric | Recorded value |
|---|---:|
| Samples | 719928 |
| Duration | 1799.981 s |
| Reported sensor errors / overflows | 0 / 0 |
| Overall mean | 3126688.361 Hz |
| Overall standard deviation | 42.730 Hz |
| Overall maximum | 3141170.561 Hz, at t=0 |
| Mean after first 10 s excluded | 3126688.653 Hz |
| Population standard deviation after first 10 s | 39.017 Hz |
| Min / max after first 10 s | 3126571.745 / 3126798.570 Hz |

The initial peak is a startup observation, not an ongoing spike. These data verify acquisition continuity in this setup; frequency variation cannot be converted to micrometre accuracy without distance calibration and controlled geometry.

Host-only evidence paths: ~/banco-eddy/eddy-estabilidad-usb.csv; reported backup ~/banco-eddy/printer-usb-eddy-directo-validado.cfg. The via-EBB backup command to ~/banco-eddy/printer-usb-eddy-via-ebb.cfg was supplied, but its execution was not shown. Raw CSV and full configs are not uploaded to this repository.

## Camera bring-up and USB disruption

Delivered camera: Innomaker-U30CAM-4K-S1, VID:PID 0bda:5883, serial 20010101, uvcvideo driver; /dev/video0 capture node and /dev/video1 additional node. Stable capture path reported by Crowsnest:
 /dev/v4l/by-id/usb-InnoMaker_Innomaker-U30CAM-4K-S1_20010101-video-index0.

Initial power-up with camera connected did not answer ping. This did not distinguish boot failure from loss of Wi-Fi. Hot-plug at uptime ~123 s produced clear tt error -71 and disconnected/re-enumerated the hub branch containing EBB and Eddy. Camera enumerated successfully; Manta was not disconnected in that initial event. Klipper subsequently reported Failed automated reset of MCU 'EBB'. FIRMWARE_RESTART restored Ready. Cause remains unproven: do not label this confirmed undervoltage, bandwidth exhaustion or kernel fault.

30-second ffmpeg test:

```bash
ffmpeg -hide_banner -f v4l2 -input_format mjpeg \
  -video_size 640x480 -framerate 15 -i /dev/video0 \
  -t 30 -an -c:v copy -f null -
```

The driver selected 30 fps despite 15 requested. 896 frames, 30.04 s, ~43818 KiB; one corrupt-buffer warning at startup. No new USB disconnect during this capture; Klipper remained Ready. Copy mode did not decode/inspect all frames. USB reconnects at uptime ~388 s preceded capture start ~415 s and coincided with firmware-restart work.

Camera-reported MJPEG modes include 4K30, 1440p30, 1080p60 and 720p30/50/60; these higher modes are advertised by V4L2, not sustained bench passes. Focus controls were disabled by the driver with UVC non-compliance errors. Focus range and final framing remain untested. Recurring eth0 No PHY found messages are the pre-existing Ethernet issue, separate from this USB result; SSH used Wi-Fi.

## Crowsnest and Mainsail

Crowsnest v5.0.4-1-g250dcde initially exhausted service retries because no usable camera existed at its startup. Recovery after camera enumeration:

```bash
sudo systemctl reset-failed crowsnest
sudo systemctl restart crowsnest
```

Observed configuration:

```ini
[crowsnest]
log_level: verbose
rollover_on_start: false
no_proxy: false

[cam 1]
mode: ustreamer
port: 8080
device: /dev/video0
resolution: 640x480
max_fps: 15
```

ustreamer listens on 127.0.0.1:8080, not the LAN address. Local snapshot and web-proxy snapshot both returned HTTP 200 (~50 KB). Access from the PC is through Mainsail's web proxy:

| Mainsail camera setting | Value |
|---|---|
| Name | Main camera |
| Service | MJPEG Stream |
| Stream URL | /webcam/?action=stream |
| Snapshot URL | /webcam/?action=snapshot |

Direct LAN access to port 8080 fails by design in this observed binding; no firewall/binding change is needed. Video was visible in the Mainsail dashboard, displaying 15 FPS; Eddy MCU temperature was 44.7 °C. This is UI output rate, not proof of camera acquisition at 15 fps.

## Reboot and cold-start results

At session close the operator reported both tests worked with the camera connected:
1. sudo reboot.
2. sudo poweroff, then PSU off/on.

The initial no-ping condition was not reproduced. Long-term stability and root cause remain open; do not describe the initial fault as conclusively fixed.

## Resume next session

1. Power the unchanged USB bench and confirm Mainsail Ready, all persistent MCU IDs and moving video.
2. Keep current 640x480 camera settings; leave the live video open.
3. Run a separate 30-minute Eddy capture to ~/banco-eddy/eddy-estabilidad-usb-via-ebb.csv; preserve direct-USB baseline. Keep sensor/metal target geometry fixed and record temperature.
4. Compare after excluding initial 10 s; record samples, errors/overflows, duration, frequency statistics, new kernel USB messages and final Klipper state.
5. Retain raw CSV, full printer.cfg, crowsnest.conf, MCU build settings and logs before marking the USB bench complete.
6. Test 3/5/10 mm spacer response when printed; no final height/homing calibration on kinematics:none.
7. Only then prepare direct CAN migration and rollback; CEB remains the later third bench.
