

add_library(${PROJECT_NAME} SHARED
        Library/include/LibraryTemplate/Library.hpp
        Library/src/Library.cpp
)
target_include_directories(${PROJECT_NAME}
    PUBLIC Library/include/
    PRIVATE Library/include/${PROJECT_NAME}
)
target_link_libraries(${PROJECT_NAME}
        PUBLIC
        PRIVATE
)
target_compile_definitions(${PROJECT_NAME}
        PUBLIC NAME="World"
        PRIVATE
)