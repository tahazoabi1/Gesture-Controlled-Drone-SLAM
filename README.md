# Hand-Controlled Drone Simulation with ORB-SLAM3

## Description
A computer vision project that uses webcam-based hand tracking to simulate drone control and perform SLAM (Simultaneous Localization and Mapping) with ORB-SLAM3.

## Structure
- `hand_tracking/`: Hand gesture recognition using MediaPipe.
- `drone_simulation/`: Virtual drone follows the hand.
- `video_recording/`: Records video for SLAM.
- `slam_input/`: Prepares/feeds video into ORB-SLAM3.
- `orb_slam3/`: Configuration and run commands.
- `videos/`: Saved input videos.
- `results/`: Output maps and trajectory files.
- `camera_forwarder/`: **[New] Web-based helper tool for streaming camera feed from a mobile device or browser to the server.**

---

## Camera Forwarder Helper

The `camera_forwarder/` folder contains a helper web app and Node.js server for forwarding real-time camera frames from any device on the network to your main project.

**Use cases:**
- Stream your phone’s or laptop’s camera to the drone simulation system.
- Useful when the main machine does not have a webcam, or you want to use a better mobile camera.

**How to use:**
See [`camera_forwarder/README.md`](camera_forwarder/README.md) for setup and streaming instructions, including security notes.

---

# Gesture-Controlled-Drone-SLAM

