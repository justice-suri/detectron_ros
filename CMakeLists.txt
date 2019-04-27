cmake_minimum_required(VERSION 2.8.3)
project(detectron_ros)

find_package(catkin REQUIRED COMPONENTS
   cv_bridge
   image_transport
   message_generation
   rospy
   sensor_msgs
   std_msgs
)

catkin_python_setup()

generate_messages(
   DEPENDENCIES
   std_msgs
   sensor_msgs
)


catkin_install_python(PROGRAMS
   src/detectron_ros/run
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
