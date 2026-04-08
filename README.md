[![CI](https://github.com/LiCS-KARPE/libmotioncapture/actions/workflows/CI.yml/badge.svg?branch=main)](https://github.com/LiCS-KARPE/libmotioncapture/actions/workflows/CI.yml)

# libmotioncapture

Interface abstraction for motion capture system APIs.

Supported backends include Motion Analysis (Cortex), Vicon, OptiTrack, Qualisys, VRPN, Nokov, and FZMotion.

## ROS2 Integration

This branch targets ROS2 with `ament_cmake` and provides:

- Python bridge node: `scripts/mocap_bridge.py`
- ROS2 launch file: `launch/mocap_bridge.launch.py`
- Python bindings package: `motioncapture_ros`

## Prerequisites

```bash
sudo apt install libboost-system-dev libboost-thread-dev libeigen3-dev
```

ROS2 environment (Humble/Jazzy or compatible) and `colcon` are required.

## Build (ROS2 / colcon)

```bash
mkdir -p ~/mocap_ws/src
cd ~/mocap_ws/src
git clone https://github.com/LiCS-KARPE/libmotioncapture.git

cd libmotioncapture
git submodule update --init

cd ~/mocap_ws
colcon build --symlink-install
source install/setup.bash
```

Enable optional backends with CMake args, for example:

```bash
colcon build --symlink-install --cmake-args -DLIBMOTIONCAPTURE_ENABLE_VICON=ON
```

## Run Bridge Node

```bash
ros2 launch libmotioncapture mocap_bridge.launch.py
```

Parameters:

- `hostname` (default: `127.0.0.1`): mocap server IP
- `type` (default: `motionanalysis`): backend type
- `topic_name` (default: `/mavros/vision_pose/pose`): output topic
- `max_radius` (default: `3.0`): max allowed distance (m)
- `fps` (default: `15.0`): publish cap (Hz)

## Examples

```bash
python3 examples/python.py motionanalysis 127.0.0.1
install/lib/libmotioncapture/motioncapture_example motionanalysis 127.0.0.1
```

## License

[MIT](LICENSE)
