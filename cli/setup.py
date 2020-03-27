from setuptools import setup


name = 'gero.cli'

install_requires = [
    'fire',
    'gero.app'
]

setup(
    name=name,
    version='0.1.0',
    author='Charles-Éric Bourget',
    author_email='charlesericbourget@gmail.com',
    description='gero cli',
    license='TBD',
    classifiers=[
        'Private :: Do Not Upload to pypi server'
    ],
    namespace_packages=['gero'],
    packages=[name],
    install_requires=install_requires,
    entry_points={
        'console_scripts': 'gero = gero.cli.cli:main'
    }
)
