import os
import sys
from setuptools import setup


DISTNAME = 'iced'
DESCRIPTION = 'ICE normalization'
MAINTAINER = 'Nelle Varoquaux'
MAINTAINER_EMAIL = 'nelle.varoquaux@gmail.com'
VERSION = "0.6.0a0.dev0"
LICENSE = "BSD"


SCIPY_MIN_VERSION = '0.19.0'
NUMPY_MIN_VERSION = '1.16.0'


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
)

