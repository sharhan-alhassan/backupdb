from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup (
    name='backupdb',
    version='0.0.1',
    author='Sharhan Alhassan',
    author_email='sharhanalhassan@gmail.com',
    description='A simple CLI utility for backing up PostgreSQL databases.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sharhan-alhassan/backupdb',
    packages=find_packages('src'),
)