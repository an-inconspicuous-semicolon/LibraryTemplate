include(GenerateExportHeader)

set(LIBRARY_INCLUDE_PATH "Library/include")
set(LIBRARY_SOURCE_PATH "Library/src")

string(TOUPPER ${PROJECT_SHORT_NAME} PROJECT_UPPER_NAME)

# ----- Make Relevant Directories
file(MAKE_DIRECTORY ${LIBRARY_INCLUDE_PATH}/${PROJECT_NAME})

