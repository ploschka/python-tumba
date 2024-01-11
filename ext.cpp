#include <pybind11/pybind11.h>

#include <pycom/lib/Pycom.hpp>

#include <llvm/Support/FileSystem.h>

#include <iostream>
#include <filesystem>
#include <fstream>


int compile_and_put_in(std::string filepath, std::string output_dir) {
    if (!std::filesystem::exists(filepath))
    {
        std::cerr << "File " << filepath << " does not exist!\n";
        return -1;
    }
    if (std::filesystem::is_directory(filepath))
    {
        std::cerr << filepath << " is a directory!\n";
        return -1;
    }

    auto errmng = std::make_unique<ErrorManager>(std::cerr);
    Pycom pycom(errmng.get());

    std::ifstream file(filepath);

    std::error_code EC;
    llvm::raw_fd_ostream output(output_dir + "output.o", EC, llvm::sys::fs::OF_None);

    pycom.open(file);
    if (pycom.checkSemantics())
    {
        pycom.generate();
        pycom.compile(output, llvm::OptimizationLevel::O0, llvm::PIELevel::Default, llvm::PICLevel::NotPIC);
    }
    return 0;
}

PYBIND11_MODULE(pycom_api, m) {
    m.doc() = "Python compilator"; // Optional module docstring
    m.def("compile_and_put_in", &compile_and_put_in, "Compile file and put it in given directory as object file");
}