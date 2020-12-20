"""Standard setup.py file for installing optoolbox module."""
from __future__ import print_function


import setuptools

REQS_FILENAME = "requirements.txt"
SETUP_FILENAME = "requirements-setup.txt"

def make_deps(filename):
    """Generate the install_requires parameter."""
    with open(filename) as fhandle:
        return fhandle.readlines()


def main():

    setuptools.setup(
        name='GIF-U003_Fonctionnel',
        author='Milan Assuied',
        description='Laval University Course',
        packages=setuptools.find_packages(exclude=("tests",)),
        install_requires=make_deps(REQS_FILENAME),
        python_requires='>= 3.8',
        setup_requires=make_deps(SETUP_FILENAME),
    )

if __name__ == '__main__':
    main()
