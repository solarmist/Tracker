from setuptools import setup

setup(
    name='Dietzilla',
    version='0.1',
    long_description=__doc__,
    packages=['self_quant'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'nose', 'flask-sqlalchemy']
)
