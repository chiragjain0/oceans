cmake_minimum_required(VERSION 3.5)
project(oceans)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

include_directories(include)

add_executable(talker src/publisher_member_function.cpp)
add_executable(bs_talker src/bspline_calc.cpp)
# add_executable(llm_list scripts/llm.py)

ament_target_dependencies(talker rclcpp std_msgs)
ament_target_dependencies(bs_talker rclcpp std_msgs)

install(TARGETS
  talker
  DESTINATION lib/${PROJECT_NAME})

install(TARGETS
  bs_talker
  DESTINATION lib/${PROJECT_NAME})

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  scripts/llm.py
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/mic.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()