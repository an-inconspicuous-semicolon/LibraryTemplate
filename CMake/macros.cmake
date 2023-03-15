
# https://stackoverflow.com/a/71169735/12940529
# Changed to lower snake_case
macro(get_subdirectories result current_directory)
    FILE(GLOB children ${current_directory}/*)
    SET(directory_list "")
    FOREACH(child ${children})
        IF(IS_DIRECTORY ${child})
            LIST(APPEND directory_list ${child})
        ENDIF()
    ENDFOREACH()
    SET(${result} ${directory_list})
ENDMACRO()