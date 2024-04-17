from cmake_build_extension import BuildExtension, CMakeExtension
from setuptools import setup

setup(
    ext_modules=[
        CMakeExtension(
            name="CMakeProject",
            install_prefix="tumba",
            cmake_depends_on=["pybind11"],
            disable_editable=True,
            cmake_configure_options=[
            ],
        )
    ],
    cmdclass=dict(build_ext=BuildExtension),
)
