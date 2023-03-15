
get_subdirectories(TESTING_DIRECTORIES ${CMAKE_CURRENT_SOURCE_DIR}/Dependencies)
foreach(DIRECTORY ${TESTING_DIRECTORIES})
    add_subdirectory(${DIRECTORY})
endforeach()
