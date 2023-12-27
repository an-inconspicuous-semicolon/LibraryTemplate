find_package(Python COMPONENTS Interpreter)

if (NOT Python_FOUND)
    message(FATAL_ERROR "Precompiled headers functionality requires python to be installed")
endif ()

function(generate_precompiled_header target_name)
    add_custom_target(${target_name}_precompiled_header
            WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
            COMMENT "Running Python script for precompiled headers"
            COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/CMake/precompiled_headers.py ${target_name} "${CMAKE_CURRENT_BINARY_DIR}/__${target_name}_sources.txt" "${CMAKE_CURRENT_BINARY_DIR}/__${target_name}_pch.hpp"
    )

    execute_process(
            WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
            COMMAND ${Python_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/CMake/precompiled_headers.py ${target_name} "${CMAKE_CURRENT_BINARY_DIR}/__${target_name}_sources.txt" "${CMAKE_CURRENT_BINARY_DIR}/__${target_name}_pch.hpp"
    )

    add_dependencies(${target_name} ${target_name}_precompiled_header)
    target_precompile_headers(${target_name} PRIVATE "${CMAKE_CURRENT_BINARY_DIR}/__${target_name}_pch.hpp")
endfunction()