#!/usr/bin/env python3
import rospy
import motioncapture_ros as motioncapture
import numpy as np
from geometry_msgs.msg import PoseStamped


def run():
    rospy.init_node("mocap_bridge_py")

    mocap_ip = rospy.get_param("~hostname", "127.0.0.1")
    mocap_type = rospy.get_param("~type", "motionanalysis")
    pub_topic = rospy.get_param("~topic_name", "/mavros/vision_pose/pose")
    max_radius = rospy.get_param("~max_radius", 3.0)
    target_fps = rospy.get_param("~fps", 15.0)

    min_interval = 1.0 / target_fps
    last_pub_time = 0.0

    pose_pub = rospy.Publisher(pub_topic, PoseStamped, queue_size=1)

    cfg = {
        "hostname": mocap_ip,
        "cortex_port": "1510",
        "multicast_port": "1511",
    }

    try:
        mc = motioncapture.connect(mocap_type, cfg)
    except Exception as e:
        rospy.logerr(f"Connection Failed: {e}")
        return

    rospy.loginfo(
        f"Connected to {mocap_type} @ {mocap_ip}, "
        f"publishing to '{pub_topic}' at max {target_fps} Hz"
    )

    while not rospy.is_shutdown():
        mc.waitForNextFrame()

        current_time = rospy.get_time()
        if (current_time - last_pub_time) < min_interval:
            continue

        last_pub_time = current_time

        for name, obj in mc.rigidBodies.items():
            pos_m = obj.position
            distance = np.linalg.norm(pos_m)

            if distance > max_radius:
                continue

            msg = PoseStamped()
            msg.header.stamp = rospy.Time.now()
            msg.header.frame_id = "map"

            msg.pose.position.x = pos_m[0]
            msg.pose.position.y = pos_m[1]
            msg.pose.position.z = pos_m[2]

            msg.pose.orientation.x = obj.rotation.x
            msg.pose.orientation.y = obj.rotation.y
            msg.pose.orientation.z = obj.rotation.z
            msg.pose.orientation.w = obj.rotation.w

            pose_pub.publish(msg)


if __name__ == "__main__":
    try:
        run()
    except rospy.ROSInterruptException:
        pass
