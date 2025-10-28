cmake_minimum_required(VERSION 3.5)
project(avion)

# Encuentra dependencias de ROS 2
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(ignition-gazebo6 REQUIRED)


# Instala los archivos de launch
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Instala modelos y mundos
install(DIRECTORY models/
  DESTINATION share/${PROJECT_NAME}/models
)

# Finaliza
ament_package()
