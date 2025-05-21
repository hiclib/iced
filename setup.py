from setuptools import Extension, setup
import numpy as np


setup(
    ext_modules=[
        Extension(name="iced._filter_",
                  sources=["iced/_filter_.pyx"],
                  include_dirs=[np.get_include()]),
        Extension(name="iced.normalization._normalization_",
                  sources=["iced/normalization/_normalization_.pyx"],
                  include_dirs=[np.get_include()]
                  )],
)
