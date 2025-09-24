from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension("fastStructure", ["fastStructure.pyx"], include_dirs=[numpy.get_include(), "vars", "."]),
    Extension("parse_bed", ["parse_bed.pyx"], include_dirs=[numpy.get_include(), "."]),
    Extension("parse_str", ["parse_str.pyx"], include_dirs=[numpy.get_include(), "."]),
    Extension("vars.admixprop", ["vars/admixprop.pyx", "vars/C_admixprop.c"], include_dirs=[numpy.get_include(), "vars"]),
    Extension("vars.allelefreq", ["vars/allelefreq.pyx", "vars/C_allelefreq.c"], 
              libraries=["gsl", "gslcblas"], extra_compile_args=["-O3"], include_dirs=[numpy.get_include(), "vars"]),
    Extension("vars.marglikehood", ["vars/marglikehood.pyx", "vars/C_marglikehood.c"], include_dirs=[numpy.get_include(), "vars"]),
    Extension("vars.utils", ["vars/utils.pyx"], include_dirs=[numpy.get_include(), "vars"]),
]

setup(
    name="fastStructure3",
    version="0.0.1",
    ext_modules=cythonize(ext_modules),
    py_modules=["chooseK", "distruct", "structure"],
    packages=["vars"], 
    include_dirs=[numpy.get_include(), "vars", "."],
    license="MIT",
    description="Python3 compatible update of Anil Raj's fastStructure",
)
