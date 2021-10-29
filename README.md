backupdb
=========

An open-source CLI tool for backing up RDS Locally or to Amazon S3 bucket

## Usage 
You will pass in the following on the command line:
- The CLI command `backup`
- The `database URL` you need to connect to 
- The `storage driver (S3 or Local)`
- The `destination (S3 bucket or local path)`
- 

## Example usage for S3 backup
```bash
$ backupdb postgres://me@example.com:5432/db --driver s3 mybucket01
```

## Example usage for Local backup
```bash
$ backupdb postgres://me@example.com:5432/db --driver local /var/local/db/backups
```

## Installation From Source
To install the package after you've cloned the repository, you'll
want to run the following command from within the project directory:
```
$ pip install --user -e .
```
## Preparing for Development
Follow these steps to start developing with this project:
1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:sharhan-alhassan/backupdb`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`