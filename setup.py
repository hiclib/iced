import os
import sys
from setuptools import Extension, setup, find_packages
import numpy as np


DISTNAME = 'iced'
DESCRIPTION = 'ICE normalization'
MAINTAINER = 'Nelle Varoquaux'
MAINTAINER_EMAIL = 'nelle.varoquaux@gmail.com'

VERSION = "0.5.13"
LICENSE = "BSD"


SCIPY_MIN_VERSION = '0.19.0'
NUMPY_MIN_VERSION = '1.16.0'

extension_config = {
    "_filter": [
        {"sources": ["_filter.pyx"]}
    ],
    "normalization": [
        {"sources": ["_normalization.pyx"]}
    ]
}


setup(
    name=DISTNAME,
    version=VERSION,
    author=MAINTAINER,
    author_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    packages=find_packages(where="."),
    ext_modules=[
        Extension(name="iced._filter_",
                  sources=["iced/_filter_.pyx"],
                  include_dirs=[np.get_include()]
        ),
        Extension(name="iced.normalization/_normalization_",
                  sources=["iced/normalization/_normalization_.pyx"],
                  include_dirs=[np.get_include()]
                  )],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ice = iced.scripts.ice:main',
        ]
    }
)

