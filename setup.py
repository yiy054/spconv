from setuptools import setup, find_packages
from setuptools.extension import Extension
from pccm.extension import PCCMExtension

NAME = 'spconv'
DESCRIPTION = 'Spatially Sparse Convolution'
AUTHOR = 'Yan Yan'
AUTHOR_EMAIL = 'yanyan.sub@outlook.com'
URL = 'https://github.com/traveller59/spconv'
REQUIRES_PYTHON = '>=3.7'
VERSION = '2.3.8'

REQUIRED = [
    "numpy",
    "fire",
    "pccm>=0.4.16",
    "ccimport>=0.4.4",
    "pybind11>=2.6.0"
]

EXT_MODULES = [
    PCCMExtension(
        [],
        "spconv/core_cc",
        "spconv",
        std="c++17",
        disable_pch=True,
        verbose=True
    )
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    ext_modules=EXT_MODULES,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
)
