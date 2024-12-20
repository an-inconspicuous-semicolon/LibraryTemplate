
include(GenerateExportHeader)

function(generate_api_header target_name)
    set_target_properties(${target_name} PROPERTIES CXX_VISIBILITY_PRESET hidden)
    GENERATE_EXPORT_HEADER(${target_name} EXPORT_FILE_NAME "${CMAKE_CURRENT_SOURCE_DIR}/Library/include/${PROJECT_NAME}/api.hpp")
endfunction()