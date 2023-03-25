add_executable(${PROJECT_NAME}_client main.cpp)
target_include_directories(${PROJECT_NAME}_client
        PUBLIC
        PRIVATE)
target_link_libraries(${PROJECT_NAME}_client
        PUBLIC
        PRIVATE ${PROJECT_NAME})