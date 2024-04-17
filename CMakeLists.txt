cmake_minimum_required(VERSION 3.13)
project(python-tumba
    VERSION 0.1.0
    DESCRIPTION "Python compiler inside python code"
    LANGUAGES C CXX)

set(PYCOM_BUILD_TESTS OFF)
set(PYCOM_BUILD_EXAMPLES OFF)
set(PYCOM_BUILD_EXECUTABLE OFF)

add_subdirectory(pycom)
add_subdirectory(3rd-party/pybind11)

include_directories(${LLVM_INCLUDE_DIRS} pycom/include 3rd-party/pybind11/include)

pybind11_add_module(pycom_api "src/ext.cpp")
target_link_libraries(pycom_api PRIVATE pycomlib)

set(TUMBA_INSTDIR "${CMAKE_INSTALL_PREFIX}")
install(TARGETS token ast lexer parser semanalyzer codegen optimizer utility std run pycomlib DESTINATION "${TUMBA_INSTDIR}/pycom")
install(TARGETS pycom_api DESTINATION "${TUMBA_INSTDIR}")
