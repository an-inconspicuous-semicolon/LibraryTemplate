cmake_minimum_required(VERSION 3.0)

add_library(some_lib SHARED include/Lib.hpp src/Lib.cpp)
target_include_directories(some_lib PUBLIC include)