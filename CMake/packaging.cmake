
set(INSTALL_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/packaging/${PROJECT_NAME})

install(TARGETS ${PROJECT_NAME}
        DESTINATION ${INSTALL_DIRECTORY})

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/Testing
        DESTINATION ${INSTALL_DIRECTORY})
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/Dependencies
        DESTINATION ${INSTALL_DIRECTORY})

install(FILES
        CMake/macros.cmake
        CMake/environment.cmake
        CMake/libraries.cmake
        CMake/options.cmake
        CMake/exporting.cmake
        CMake/packaging/pre_lib.cmake
        CMake/packaging/post_lib.cmake
        CMake/templates/installing.cmake
        DESTINATION ${INSTALL_DIRECTORY}/CMake)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/CMakeLists.txt
        DESTINATION ${INSTALL_DIRECTORY})

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/Library
        DESTINATION ${INSTALL_DIRECTORY})

install(FILES
        COPYING
        COPYING.LESSER
        DESTINATION ${INSTALL_DIRECTORY})

install(CODE "execute_process(COMMAND
  python ${CMAKE_CURRENT_SOURCE_DIR}/CMake/build_info.py ${PROJECT_NAME} ${PROJECT_VERSION} OUTPUT_VARIABLE build_info)
  file(WRITE ${INSTALL_DIRECTORY}/build_info.txt \${build_info})")

install(CODE "file(ARCHIVE_CREATE OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}.zip
        PATHS ${INSTALL_DIRECTORY}
        FORMAT zip
        )")
