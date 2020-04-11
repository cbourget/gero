from setuptools import setup


name = 'gero.app'

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
    packages=[
        name,
        'gero.app.contexts',
        'gero.app.database',
        'gero.app.domain',
        'gero.app.utils'
    ],
    install_requires=install_requires
)
