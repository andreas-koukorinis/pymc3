#/usr/bin/env python  
try:
    import setuptools
except ImportError:
    pass
from numpy.distutils.core import setup, Extension


flib = Extension(name='PyMC.flib',sources=['PyMC/flib.f'])
version = "1.1"

distrib = setup(
    version=version,
    author="Chris Fonnesbeck",
    author_email="fonnesbeck@mac.com",
    description="Version %s of PyMC" % version,
    license="Academic Free License",
    name="PyMC",
    url="trichech.us",
    packages=["PyMC", "PyMC.database", "PyMC.tests"],
    ext_modules = [flib]    
)
