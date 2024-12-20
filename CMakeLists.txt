cmake_minimum_required(VERSION 3.5)

project(LibraryTemplate
        VERSION 0.1.0
        DESCRIPTION "A template for creating C++20 libraries"
        HOMEPAGE_URL "https://github.com/an-inconspicuous-semicolon/LibraryTemplate"
        LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 20)

include(CMake/exports.cmake)
add_subdirectory(CMake/pch_generator)
include(CMake/library.cmake)
include(CMake/client.cmake)

generate_api_header(${PROJECT_NAME})
generate_pch_for_target(${PROJECT_NAME})

