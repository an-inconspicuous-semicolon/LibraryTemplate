

set(CLIENT_SOURCES
        Client/main.cpp
)


if (CMAKE_BUILD_TYPE STREQUAL "Release")
    add_executable(${PROJECT_NAME}_client WIN32 ${CLIENT_SOURCES})
else ()
    add_executable(${PROJECT_NAME}_client ${CLIENT_SOURCES})
endif ()

target_include_directories(${PROJECT_NAME}_client
        PUBLIC Client/
        PRIVATE
)
target_link_libraries(${PROJECT_NAME}_client
        PUBLIC ${PROJECT_NAME}
        PRIVATE
)
target_compile_definitions(${PROJECT_NAME}_client
        PUBLIC
        PRIVATE
)