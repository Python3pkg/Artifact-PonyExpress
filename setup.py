#!/usr/bin/env python

from setuptools import setup

setup(	name='Pony',
        version='0.2.5',
        description='General purpose package manager based on MongoDB',
        author='Giuseppe Puoti',
        author_email='giuseppe.puoti@gmail.com',
        url='',
        
        py_modules=[
            'pony', 
            'bag',
            'config_constrainer',
            'dependencies',
            'alternative_set',

            'pony_scons',
            'cli'
            # list them here when you add any other modules!
            ],
            
        
        
        install_requires = [
            'tabulate', 
            'colorama', 
            'networkx',
            'pymongo'
            # add any other dependency package here in order to let pip install them as installation' side effect.
            ],
            
        scripts = ['pony.py']  
)