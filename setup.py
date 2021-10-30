from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup (
    name='backupdb',
    version='0.0.5',
    author='Sharhan Alhassan',
    author_email='sharhanalhassan@gmail.com',
    description='A simple CLI utility for backing up PostgreSQL databases.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sharhan-alhassan/backupdb',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[requirements],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': [
            'backupdb=backupdb.cli:main',
        ],
    }
)