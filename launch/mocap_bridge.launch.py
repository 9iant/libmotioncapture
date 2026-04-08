from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="libmotioncapture",
                executable="mocap_bridge.py",
                name="mocap_bridge",
                output="screen",
                parameters=[
                    {
                        "hostname": "127.0.0.1",
                        "type": "motionanalysis",
                        "topic_name": "/mavros/vision_pose/pose",
                        "max_radius": 3.0,
                        "fps": 15.0,
                    }
                ],
            )
        ]
    )
