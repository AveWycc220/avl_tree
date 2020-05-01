""" Setup module """ 
from setuptools import setup, find_packages

setup(
    name='AVLTreeSet',
    version='1.0',
    url='https://github.com/AveWycc220',
    license='MIT',
    author='Aleksey Guzenko',
    author_email='mik16748@gmail.com',
    description='Set implemented on avl-tree.',
    packages=find_packages(),
    long_description=open('README.md').read(),
    zip_safe=False,
)
