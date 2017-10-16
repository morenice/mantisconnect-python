from setuptools import setup
from setuptools import find_packages
import os
import mantisconnect


setup(name=mantisconnect.__module_name__,
      version=mantisconnect.__version__,
      description=mantisconnect.__doc__.strip(),
      author='morenice',
      author_email='hyoungguyo@hotmail.com',
      url='https://github.com/morenice/mantisconnect-python',
      license=mantisconnect.__license__,
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      python_requires='>=3',
      classifiers=[
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Software Development',
                   'Topic :: Utilities'
                   ]
      )
