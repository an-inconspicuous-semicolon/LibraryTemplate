cmake_minimum_required(VERSION 3.12)
project(LibraryTemplate
        VERSION 0.1.0.0
        DESCRIPTION "A Template Library"
        HOMEPAGE_URL "https://github.com/an-inconspicuous-semicolon/LibraryTemplate"
        LANGUAGES CXX)
set(PROJECT_SHORT_NAME tmplt)

include(CMake/macros.cmake)
include(CMake/environment.cmake)
include(CMake/libraries.cmake)

set(CMAKE_CXX_STANDARD 20)

add_library(${PROJECT_NAME} SHARED Library/src/library.cpp ${LIBRARY_INCLUDE_PATH}/${PROJECT_NAME}/api.hpp Library/include/LibraryTemplate/library.hpp Dependencies/some_lib/src/Lib.cpp Dependencies/some_lib/include/Lib.hpp)
target_include_directories(LibraryTemplate
        PUBLIC ${LIBRARY_INCLUDE_PATH}
        PRIVATE ${LIBRARY_INCLUDE_PATH}/${PROJECT_NAME})
target_link_libraries(LibraryTemplate
        PUBLIC
        PRIVATE some_lib)

include(CMake/options.cmake)
include(CMake/exporting.cmake)
include(CMake/testing.cmake)
include(CMake/packaging.cmake)