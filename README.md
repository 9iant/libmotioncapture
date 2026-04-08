[![CI](https://github.com/9iant/libmotioncapture/actions/workflows/CI.yml/badge.svg?branch=main)](https://github.com/9iant/libmotioncapture/actions/workflows/CI.yml)

# libmotioncapture

Interface abstraction for motion capture system APIs.

Supported backends include Motion Analysis (Cortex), Vicon, OptiTrack, Qualisys, VRPN, Nokov, and FZMotion.

## ROS1 Integration

This branch targets ROS1 with `catkin` and provides:

- Python bridge node: `scripts/mocap_bridge.py`
- ROS1 launch file: `launch/mocap_bridge.launch`
- Python bindings package: `motioncapture_ros`

## Prerequisites

```bash
sudo apt install libboost-system-dev libboost-thread-dev libeigen3-dev
```

ROS1 environment (Noetic or compatible) and `catkin` are required.

## Build (ROS1 / catkin)

```bash
mkdir -p ~/mocap_ws/src
cd ~/mocap_ws/src
git clone https://github.com/9iant/libmotioncapture.git

cd libmotioncapture
git submodule update --init

cd ~/mocap_ws
catkin_make
source devel/setup.bash
```

Enable optional backends with CMake args, for example:

```bash
catkin_make -DLIBMOTIONCAPTURE_ENABLE_VICON=ON
```

## Run Bridge Node

```bash
roslaunch libmotioncapture mocap_bridge.launch
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
devel/lib/libmotioncapture/motioncapture_example motionanalysis 127.0.0.1
```

## License

[MIT](LICENSE)
