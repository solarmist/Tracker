import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Dietzilla',
    version='0.1',
    author='Joshua Olson',
    author_email='joshua.olson@gmail.com',
    description=('A website for tracking trends in data, '
                 'mainly weight loss/gain'),
    long_description=read('README'),
    packages=['self_quant', 'test'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask >= 0.9',
                      'nose',
                      'sphinx',
                      'sqlalchemy >= 0.7.7',
                      'psycopg2',
                      'flask-sqlalchemy',
                      'sqlalchemy-migrate'],
    classifiers=[
        'Natural Language :: English',
        'Development Status :: 1 - Planning'
        ]

)
