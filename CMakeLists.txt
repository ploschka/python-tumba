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

#/------LLVM------/
find_package(LLVM REQUIRED CONFIG)
separate_arguments(LLVM_DEFINITIONS_LIST NATIVE_COMMAND ${LLVM_DEFINITIONS})
add_definitions(${LLVM_DEFINITIONS_LIST})
foreach(target ${LLVM_TARGETS_TO_BUILD})
  list(APPEND targets "LLVM${target}CodeGen")
endforeach()
list(APPEND target_asmparsers LLVMX86AsmParser)
llvm_map_components_to_libnames(llvm_libraries analysis support core object irreader executionengine scalaropts instcombine orcjit runtimedyld)
#/------LLVM------/

pybind11_add_module(pycom_api ext.cpp)
target_link_libraries(pycom_api PRIVATE pycomlib)

install(TARGETS pycom_api DESTINATION ${CMAKE_SOURCE_DIR})