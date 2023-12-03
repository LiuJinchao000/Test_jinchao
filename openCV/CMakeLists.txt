cmake_minimum_required(VERSION 3.2)
 
project(hello-cmake)
 
#list(APPEND CMAKE_PREFIX_PATH "/home/liu/anaconda3/envs/DisplayImage")  # apt装的opencv
#list(APPEND CMAKE_PREFIX_PATH "/usr/local/opencv-git-master")   #自行编译的opencv
message("CMAKE_MODULE_PATH is: ${CMAKE_MODULE_PATH}")
find_package(OpenCV
    #NO_CMAKE_PATH
    #NO_CMAKE_ENVIRONMENT_PATH
    #NO_SYSTEM_ENVIRONMENT_PATH
    #NO_CMAKE_PACKAGE_REGISTRY
    #NO_CMAKE_SYSTEM_PATH
    )
message("OpenCV_FOUND is : ${OpenCV_FOUND}")
message("OpenCV_INCLUDE_DIRS is : ${OpenCV_INCLUDE_DIRS}")
message("OpenCV_INCLUDES is : ${OpenCV_INCLUDES}")
message("OpenCV_LIBRARIES is ${OpenCV_LIBRARIES}")
message("OpenCV_LIBS is : ${OpenCV_LIBS}")
message("OpenCV_DEFINITIONS is : ${OpenCV_DEFINITIONS}")
 
add_executable(hello main.cpp)
 
target_link_libraries(hello ${OpenCV_LIBS})
 