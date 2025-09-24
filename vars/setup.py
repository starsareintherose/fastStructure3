from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension("vars.admixprop", ["admixprop.pyx", "C_admixprop.c"], include_dirs=[numpy.get_include(), '.']),
    Extension("vars.allelefreq", ["allelefreq.pyx", "C_allelefreq.c"], 
              libraries=["gsl", "gslcblas"], extra_compile_args=["-O3"], include_dirs=[numpy.get_include(), '.']),
    Extension("vars.marglikehood", ["marglikehood.pyx", "C_marglikehood.c"], include_dirs=[numpy.get_include(), '.']),
    Extension("vars.utils", ["utils.pyx"], include_dirs=[numpy.get_include(), '.']),
]

setup(
    name="variables",
    version="1.0",
    ext_modules=cythonize(ext_modules),
    packages=["vars"],
    include_dirs=[numpy.get_include(), '.'],
)
