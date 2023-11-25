cmake_minimum_required(VERSION 2.8)
project( demo_all )
SET(ROOT_DIR ${CMAKE_SOURCE_DIR})
aux_source_directory(. DIR_SRCS)
INCLUDE_DIRECTORIES(${ROOT_DIR})
add_executable(demo_all ${DIR_SRCS})

