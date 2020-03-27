from setuptools import setup


name = 'gero.api'

install_requires = [
    'pyjwt',
    'capri.falcon',
    'gero.app'
]

setup(
    name=name,
    version='0.1.0',
    author='Charles-Éric Bourget',
    author_email='charlesericbourget@gmail.com',
    description='gero api',
    license='TBD',
    classifiers=[
        'Private :: Do Not Upload to pypi server'
    ],
    namespace_packages=['gero'],
    packages=[name],
    install_requires=install_requires
)
