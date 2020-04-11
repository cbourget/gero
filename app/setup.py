import os 

from setuptools import setup, find_packages

name = 'gero.app'
here = os.path.dirname(os.path.realpath(__file__))
packages = [name].concat(
    find_packages(f'{here}/{name.replace('.', '/')}')
)

install_requires = [
    'capri.utils',
    'capri.core',
    'capri.alchemy',

    'psycopg2'
]

setup(
    name=name,
    version='0.1.0',
    author='Charles-Éric Bourget',
    author_email='charlesericbourget@gmail.com',
    description='gero App',
    license='TBD',
    classifiers=[
        'Private :: Do Not Upload to pypi server'
    ],
    namespace_packages=['gero'],
    packages=packages,
    install_requires=install_requires
)
