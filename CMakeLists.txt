cmake_minimum_required(VERSION 3.12)
project(LibraryTemplate
        VERSION 0.1.0.0
        DESCRIPTION "A Template Library"
        HOMEPAGE_URL "https://github.com/an-inconspicuous-semicolon/LibraryTemplate"
        LANGUAGES CXX)
set(PROJECT_SHORT_NAME tmplt)

include(CMake/pre_lib.cmake)

set(CMAKE_CXX_STANDARD 20)

add_library(${PROJECT_NAME} SHARED Library/src/library.cpp ${LIBRARY_INCLUDE_PATH}/${PROJECT_NAME}/api.hpp Library/include/LibraryTemplate/library.hpp)
target_include_directories(${PROJECT_NAME}
        PUBLIC ${LIBRARY_INCLUDE_PATH}
        PRIVATE ${LIBRARY_INCLUDE_PATH}/${PROJECT_NAME})
target_link_libraries(${PROJECT_NAME}
        PUBLIC
        PRIVATE some_lib)

include(CMake/post_lib.cmake)
