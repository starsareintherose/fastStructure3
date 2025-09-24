from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension("fastStructure", ["fastStructure.pyx"], include_dirs=[numpy.get_include(), "vars", "."]),
    Extension("parse_bed", ["parse_bed.pyx"], include_dirs=[numpy.get_include(), "."]),
    Extension("parse_str", ["parse_str.pyx"], include_dirs=[numpy.get_include(), "."]),
]

setup(
    name="fastStructure3",
    version="0.0.1",
    ext_modules=cythonize(ext_modules),
    py_modules=["chooseK", "distruct", "structure"],
    license="MIT",
    description="Python3 compatible update of Anil Raj's fastStructure",
)
