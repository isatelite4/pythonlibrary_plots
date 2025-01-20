from setuptools import find_packages, setup

setup(
    name='plotsetups_me',
    packages=find_packages(include=['plotsetups_me']),
    version='0.1.0',
    description='Library with some functions for customize plots. Includes 18 ds9 colormaps.',
    author='Ignacio Ruiz',
    install_requires=['numpy','matplotlib'],
    setup_requires=['pytest-runner'],
    test_suite='tests',
)