# Generation 3 main frame camera

## Frozen selection

The Generation 3 primary frame camera is the **Innomaker U30CAM-4K-S1** USB UVC camera module.

This selection supersedes the earlier CSI-first / model-open camera concept. Those references are obsolete for the primary frame camera. CSI may still be evaluated for unrelated future imaging experiments, but it is no longer the baseline for the main camera.

### Identification

- Manufacturer: Innomaker
- Model: **U30CAM-4K-S1**
- Amazon ES ASIN: **B0FQJB4Z79**
- Sensor: **Sony IMX415 STARVIS**, approximately 8 MP
- Host interface: **USB 3.0, UVC**, with USB 2.0 backward compatibility
- Advertised primary video modes: **3840 × 2160 at 30 fps** and **1920 × 1080 at 60 fps**
- Advertised formats include **MJPEG** and **YUY2**
- Lens: wide-angle, adjustable focus
- Approximate field of view: **105° horizontal / 116° diagonal**
- Approximate PCB size: **38 × 38 mm**

The exact modes, frame rates, pixel formats and controls exposed by the delivered unit are not treated as bench-verified until queried with V4L2.

## Host compatibility and migration

The camera is deliberately USB/UVC so the same main camera can survive Linux-host changes without depending on a CSI sensor driver or device-tree overlay.

Planned host progression:

1. **CB1 bench stage:** connect as a standard Linux UVC camera. Start validation at 1920 × 1080 MJPEG / 30 fps, then test 60 fps and higher modes while observing host load, temperature, latency and Klipper stability.
2. **CB2 final target:** retain the same UVC camera; use the best validated USB path and reassess 4K30 / 1080p60 operation.
3. **CM4 alternative:** retain UVC compatibility if CM4 is selected instead of CB2; achievable high-rate modes remain dependent on the actual USB topology and compressed format.

A mode being advertised by the camera does not by itself prove that a given host/topology can sustain it reliably.

## Mechanical integration

The camera remains **fixed to the printer frame**, never to the moving bed or toolhead.

Requirements:

- stable view of the complete bed/nozzle work area;
- exploit the wide-angle lens while avoiding unnecessary distortion of the useful print region;
- adjustable mount for final framing and focus;
- custom ASA enclosure with late-1980s/1990s industrial CCTV/video-surveillance language;
- no exposed modern PCB in the finished machine;
- preserve access to focus adjustment and USB service connection;
- final mount geometry is frozen only after physical framing tests on the rebuilt printer.

## Software and RID role

The main camera is a first-class input for Crowsnest/Mainsail and for **Revival Intelligence & Diagnostics (RID)**.

Normal operation should favour a resolution/frame-rate combination that leaves comfortable host margin. 4K is valuable for detailed captures, timelapse and vision regions of interest; continuous 4K operation is not a requirement.

RID may reuse the stream or selected frames for print-failure detection, first-layer inspection, anomaly evidence, fiducial/geometry checks and later vision candidates. Deterministic printer control and safety remain independent of camera/RID availability.

## Incoming bench acceptance

On receipt, record the real device rather than relying only on seller specifications:

```bash
lsusb
lsusb -t
v4l2-ctl --list-devices
v4l2-ctl --list-formats-ext -d /dev/video0
```

Then validate at minimum:

- enumeration and stable reconnect on the CB1;
- UVC/V4L2 operation;
- actual MJPEG/YUY2 mode table;
- 1080p30 baseline;
- 1080p60 if exposed;
- 4K30 if exposed, noting USB topology and host load;
- Crowsnest/Mainsail stream;
- sustained CPU load, temperature and Klipper stability;
- focus range and useful frame coverage at plausible mounting distances.

## Superseded camera assumptions

The following previous assumptions are explicitly obsolete for the **main frame camera**:

- “CSI preferred, USB permitted”;
- “camera model/interface open”;
- “select CSI first and fall back to USB if ribbon routing is difficult”;
- deferring the main sensor/lens/interface selection entirely until later framing tests.

Physical mount position and final framing remain open until the delivered U30CAM-4K-S1 is tested on the machine.
