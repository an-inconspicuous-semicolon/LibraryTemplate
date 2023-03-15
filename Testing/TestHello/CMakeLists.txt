

add_executable(test_hello test_hello.cpp)
target_link_libraries(test_hello PUBLIC ${PROJECT_NAME})

add_test(NAME test_hello.cpp COMMAND test_hello)
