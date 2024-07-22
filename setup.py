from setuptools import setup, Extension, find_packages
import sys
import os

version = '1.0.0'
requirements = [line.strip() for line in open("requirements.txt").readlines()]

setup (
        name = 'sa0lef',
        version = version,
        description = "Station config for SA0LEF",
        author = 'Leif Johansson',
        author_email = 'leifj@mnt.se',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        include_package_data=True,
        provides = ['sa0lef'],
        install_requires = requirements
       )
