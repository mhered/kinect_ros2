# Testing my Kinect Lite

forked from https://github.com/thallesgate/kinect_ros2 

Made `jazzy` the default branch and deleted `galactic` branch

To install the package "The good way&trade;" clone it to folder `~/git` and symlink to your workspace:

```bash
$ cd ~/git
$ git clone https://github.com/mhered/kinect_ros2.git

$ ln -s ~/git/kinect_ros2 ~/dev_ws/src/kinect_ros
```

Build the workspace:

```bash
$ cd ~/dev_ws
$ source install/setup.bash
$ colcon build --symlink-install
```

Note: I later updated the repo with commits from https://github.com/NickelsLab/kinect_ros2 to silence some warnings

When we plug the full Kinect and read the kernel message we see a USB Hub is detected with 3 devices: a Xbox NUI Motor, a Xbox Kinect Audio and the **Xbox NUI Camera**, which is the one we are interested  in

```bash
$ sudo dmesg -w
...
# plug in the Kinect
[736340.115703] usb 3-3: new high-speed USB device number 107 using xhci_hcd
[736340.239091] usb 3-3: New USB device found, idVendor=0409, idProduct=005a, bcdDevice= 1.00
[736340.239107] usb 3-3: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[736340.240864] hub 3-3:1.0: USB hub found
[736340.240931] hub 3-3:1.0: 3 ports detected
[736340.962600] usb 3-3.2: new full-speed USB device number 108 using xhci_hcd
[736341.058346] usb 3-3.2: New USB device found, idVendor=045e, idProduct=02b0, bcdDevice= 1.07
[736341.058352] usb 3-3.2: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[736341.058355] usb 3-3.2: Product: Xbox NUI Motor
[736341.058356] usb 3-3.2: Manufacturer: Microsoft
[736342.367703] usb 3-3.1: new high-speed USB device number 109 using xhci_hcd
[736342.455268] usb 3-3.1: New USB device found, idVendor=045e, idProduct=02ad, bcdDevice= 1.00
[736342.455283] usb 3-3.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[736342.455288] usb 3-3.1: Product: Xbox Kinect Audio, © 2011 Microsoft Corporation. All rights reserved.
[736342.455292] usb 3-3.1: Manufacturer: Microsoft
[736342.455295] usb 3-3.1: SerialNumber: A44885D16505103A
[736344.158742] usb 3-3.3: new high-speed USB device number 110 using xhci_hcd
[736344.246080] usb 3-3.3: New USB device found, idVendor=045e, idProduct=02ae, bcdDevice= 1.0b
[736344.246094] usb 3-3.3: New USB device strings: Mfr=2, Product=1, SerialNumber=3
[736344.246098] usb 3-3.3: Product: Xbox NUI Camera
[736344.246103] usb 3-3.3: Manufacturer: Microsoft
[736344.246106] usb 3-3.3: SerialNumber: A00365A17045103A

```

vs when we plug the Kinect Lite, only the Xbox NUI Camera is detected

```bash
# plug in Kinect Lite
[736274.013514] usb 3-4: new high-speed USB device number 106 using xhci_hcd
[736274.141426] usb 3-4: New USB device found, idVendor=045e, idProduct=02ae, bcdDevice= 1.0b
[736274.141445] usb 3-4: New USB device strings: Mfr=2, Product=1, SerialNumber=3
[736274.141450] usb 3-4: Product: Xbox NUI Camera
[736274.141454] usb 3-4: Manufacturer: Microsoft
[736274.141457] usb 3-4: SerialNumber: A00365800998039A
```

However it does not work!

The full Kinect shows camera and depth feed using the launch files provided (even if there seems to be a problem withthe TF)

The Kinect Lite does not work. No error thrown by the launch files, but no data published in the topics... 

**Do I need to build libfreenect??**