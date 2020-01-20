import roslaunch
import rospy

rospy.init_node('en_Mapping', anonymous=True)
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/nalin/geo-matrix/ros-velodyne/simulator/src/velodyne_simulator/velodyne_description/launch/example.launch"])
launch.start()
rospy.loginfo("started")
rospy.spin()

