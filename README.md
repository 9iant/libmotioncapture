[![CI](https://github.com/LiCS-KARPE/libmotioncapture/actions/workflows/CI.yml/badge.svg?branch=main)](https://github.com/LiCS-KARPE/libmotioncapture/actions/workflows/CI.yml)

# libmotioncapture

Interface Abstraction for Motion Capture System APIs.

Supports Motion Analysis (Cortex), Vicon, OptiTrack, Qualisys, VRPN, Nokov, FZMotion, and more.

This is a fork of [IMRCLab/libmotioncapture](https://github.com/IMRCLab/libmotioncapture/) with the following changes:

- Added Motion Analysis (Cortex) SDK support
- Added ROS (catkin) integration with `mocap_bridge` node
- Added Python bindings as `motioncapture_ros` ROS package
- Removed unused submodules
- Fixed orientation calculation

## Project Structure

```
libmotioncapture/
├── CMakeLists.txt            # catkin build configuration
├── package.xml               # ROS package manifest
├── version                   # version string ("1.0")
├── deps/                     # external dependencies (git submodules)
│   ├── cortex_sdk_linux/     #   Motion Analysis Cortex SDK
│   └── pybind11/             #   Python bindings library
├── include/
│   └── libmotioncapture/     # C++ header files
├── src/                      # C++ source files
│   ├── motioncapture.cpp     #   core / factory
│   ├── motionanalysis.cpp    #   Motion Analysis backend
│   ├── vicon.cpp             #   Vicon backend
│   ├── optitrack.cpp         #   OptiTrack backend
│   ├── qualisys.cpp          #   Qualisys backend
│   ├── vrpn.cpp              #   VRPN backend
│   ├── nokov.cpp             #   Nokov backend
│   ├── fzmotion.cpp          #   FZMotion backend
│   ├── mock.cpp              #   mock backend (testing)
│   └── python_bindings.cpp   #   pybind11 bindings
├── examples/
│   ├── main.cpp              # C++ usage example
│   └── python.py             # Python usage example
├── scripts/
│   └── mocap_bridge.py       # ROS node: publishes PoseStamped
├── launch/
│   └── mocap_bridge.launch   # ROS launch file
└── motioncapture_ros/
    └── __init__.py            # Python package wrapper
```

## Prerequisites

```bash
sudo apt install libboost-system-dev libboost-thread-dev libeigen3-dev
```

ROS 1 (Noetic 등) 및 catkin 빌드 환경이 필요합니다.

## Build (catkin)

```bash
# 워크스페이스 생성 (이미 있다면 생략)
mkdir -p ~/mocap_ws/src
cd ~/mocap_ws/src
git clone https://github.com/LiCS-KARPE/libmotioncapture.git

# 서브모듈 초기화
cd libmotioncapture
git submodule init
git submodule update

# 빌드
cd ~/mocap_ws
catkin_make
source devel/setup.bash
```

### CMake Options

| Option | Default | Description |
|--------|---------|-------------|
| `LIBMOTIONCAPTURE_ENABLE_MOTIONANALYSIS` | **ON** | Motion Analysis (Cortex) 백엔드 |
| `LIBMOTIONCAPTURE_ENABLE_VICON` | OFF | Vicon 백엔드 |
| `LIBMOTIONCAPTURE_ENABLE_OPTITRACK` | OFF | OptiTrack (open source) 백엔드 |
| `LIBMOTIONCAPTURE_ENABLE_OPTITRACK_CLOSED_SOURCE` | OFF | OptiTrack (NatNet SDK) 백엔드 |
| `LIBMOTIONCAPTURE_ENABLE_QUALISYS` | OFF | Qualisys 백엔드 |
| `LIBMOTIONCAPTURE_ENABLE_NOKOV` | OFF | Nokov 백엔드 |
| `LIBMOTIONCAPTURE_ENABLE_VRPN` | OFF | VRPN 백엔드 |
| `LIBMOTIONCAPTURE_ENABLE_FZMOTION` | OFF | FZMotion 백엔드 |
| `LIBMOTIONCAPTURE_BUILD_PYTHON_BINDINGS` | ON | Python 바인딩 빌드 |
| `LIBMOTIONCAPTURE_BUILD_EXAMPLE` | ON | C++ 예제 빌드 |

예시 — Vicon도 함께 활성화:

```bash
catkin_make -DLIBMOTIONCAPTURE_ENABLE_VICON=ON
```

## Usage

### ROS Launch

```bash
roslaunch libmotioncapture mocap_bridge.launch
```

Launch 파라미터:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `hostname` | `127.0.0.1` | 모션캡처 서버 IP |
| `type` | `motionanalysis` | 모션캡처 시스템 타입 |
| `topic_name` | `/mavros/vision_pose/pose` | Publish할 토픽 이름 |
| `max_radius` | `3.0` | 최대 허용 거리 (m) |
| `fps` | `15.0` | 최대 퍼블리시 주파수 (Hz) |

### Python Example

```bash
python3 examples/python.py motionanalysis 127.0.0.1
```

### C++ Example

빌드 후:

```bash
devel/lib/libmotioncapture/motioncapture_example motionanalysis 127.0.0.1
```

## License

[MIT](LICENSE)
