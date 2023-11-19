from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension("quickpixler", ["quickpixler.pyx"],
              include_dirs=[numpy.get_include()])
]

setup(
    ext_modules = cythonize(ext_modules)
)
