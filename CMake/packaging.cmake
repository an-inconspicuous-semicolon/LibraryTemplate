find_package(Python COMPONENTS Interpreter)

if (NOT Python_FOUND)
    message(FATAL_ERROR "Packaging functionality requires python to be installed")
endif ()

function(prepare_for_packaging target_name)
    set(target_file $<TARGET_FILE:${target_name}>)
    install(CODE "execute_process(COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/CMake/packaging.py ${target_name} ${target_file} ${CMAKE_CURRENT_SOURCE_DIR} ${PROJECT_VERSION})")
endfunction()

