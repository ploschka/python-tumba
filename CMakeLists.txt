cmake_minimum_required(VERSION 3.8)
project(python-tumba
    VERSION 0.1.0
    DESCRIPTION "Python compiler inside python code"
    LANGUAGES C CXX)

add_subdirectory(pycom)
add_subdirectory(3rd-party/pybind11)

set(PYCOM_BUILD_TESTS OFF)
set(PYCOM_BUILD_EXAMPLES OFF)
set(PYCOM_BUILD_EXECUTABLE  OFF)

include_directories(${LLVM_INCLUDE_DIRS} pycom/include 3rd-party/pybind11/include)

pybind11_add_module(pycom_api ext.cpp)
target_link_libraries(pycom_api PRIVATE pycomlib)
