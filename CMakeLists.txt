cmake_minimum_required(VERSION 3.8)
project(physicalai_teleop)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)

add_executable(teleop_keyboard src/teleop_keyboard.cpp)
ament_target_dependencies(teleop_keyboard rclcpp moveit_ros_planning_interface geometry_msgs tf2_geometry_msgs)

install(TARGETS teleop_keyboard
  DESTINATION lib/${PROJECT_NAME})

ament_package() 