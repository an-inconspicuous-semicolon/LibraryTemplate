
file(MAKE_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/Library/include/${PROJECT_NAME}")


macro(store_target_properties target_name)
    get_target_property(target_sources ${target_name} SOURCES)

    file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/__${target_name}_toolchain.txt" "${CMAKE_CXX_COMPILER_ID}\n${CMAKE_CXX_COMPILER_VERSION}")

    file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/__${target_name}_sources.txt" "")
    foreach (target_source ${target_sources})
        file(APPEND "${CMAKE_CURRENT_BINARY_DIR}/__${target_name}_sources.txt" "${CMAKE_CURRENT_SOURCE_DIR}/${target_source}\n")
    endforeach ()
endmacro()


