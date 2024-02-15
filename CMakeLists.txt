cmake_minimum_required(VERSION 3.27)
project(LibraryTemplate
        VERSION 1.0.2
        DESCRIPTION "A Template for creating c++ 20 libraries"
        HOMEPAGE_URL "https://github.com/an-inconspicuous-semicolon/LibraryTemplate"
        LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 20)

include(CMake/preparation.cmake)
include(CMake/precompiled_headers.cmake)
include(CMake/packaging.cmake)
include(CMake/exports.cmake)
include(CMake/client/client_prepare.cmake)

add_library(${PROJECT_NAME} SHARED
        Library/src/library.cpp
        Library/include/LibraryTemplate/library.hpp
)
target_include_directories(${PROJECT_NAME}
        PUBLIC Library/include/
        PRIVATE Library/include/${PROJECT_NAME}
)

include(CMake/client.cmake)

store_target_properties(${PROJECT_NAME})
generate_precompiled_header(${PROJECT_NAME})
prepare_for_packaging(${PROJECT_NAME})
generate_api_header(${PROJECT_NAME})
include(CMake/client/client_post_library.cmake)
