import pip
import os

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


name = 'gero.app'

install_requires = [
    'capri.utils',
    'capri.core',
    'capri.alchemy',

    'psycopg2'
]

def install_packages(packages, develop=False):
    """ Use pip to install all libraries.  """

    wd = os.getcwd()
    for package in packages:
        os.chdir(os.path.join(wd, package))

        if develop:
            pip.main(['install', '-e', '.'])
        else:
            pip.main(['install', '.'])

        os.chdir(wd)


class DevelopCmd(develop):
    """ Add custom steps for the develop command """

    def run(self):
        install_packages(packages, develop=True)
        develop.run(self)


class InstallCmd(install):
    """ Add custom steps for the install command """

    def run(self):
        install_packages(packages, develop=False)
        install.run(self)

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
    packages=[name],
    install_requires=install_requires,
    cmdclass={
        'install': InstallCmd,
        'develop': DevelopCmd
    }
)
