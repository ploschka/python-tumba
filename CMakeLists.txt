cmake_minimum_required(VERSION 3.8)
project(python-tumba
    VERSION 0.1.0
    DESCRIPTION "Python compiler inside python code"
    LANGUAGES C CXX)

set(PYCOM_BUILD_TESTS OFF)
set(PYCOM_BUILD_EXAMPLES OFF)
set(PYCOM_BUILD_EXECUTABLE  OFF)

add_subdirectory(pycom)
