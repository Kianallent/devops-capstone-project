from setuptools import setup, find_packages
setup(
    name='customer-accounts',
    version='1.0',
    packages=find_packages(),
    install_requires=['flask', 'flake8', 'nose', 'coverage', 'flask-talisman', 'flask-cors']
)