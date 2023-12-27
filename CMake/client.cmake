

add_executable(${PROJECT_NAME}_client Client/main.cpp)
target_include_directories(${PROJECT_NAME}_client PUBLIC Client/)
target_link_libraries(${PROJECT_NAME}_client PUBLIC ${PROJECT_NAME})