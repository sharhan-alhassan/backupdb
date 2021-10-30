backupdb
=========

An open-source CLI tool for backing up RDS(PostgreSQL) Locally or to Amazon S3 bucket

## Usage 
You will pass in the following on the command line:
- The CLI command `backup`
- The `database URL` you need to connect to 
- The `storage driver (S3 or Local)`
- The `destination (S3 bucket or local path)`

## Installation
```bash
$ pip install backupdb
```

## Syntax

```bash
$ backupdb postgres://[USERNAME]:[PASSWORD]@[SERVER_IP:80/<db_name> --driver <driver_type> <destination>
```

## Example usage for S3 backup
```bash
$ backupdb postgres://[USERNAME]:[PASSWORD]@[SERVER_IP:80/<db_name> --driver s3 mybucket01
```

## Example usage for Local backup
```bash
$ backupdb postgres://[USERNAME]:[PASSWORD]@[SERVER_IP:80/<db_name> --driver local /var/local/mybackup.sql
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
4. Activate virtualenv `source /venv/bin/activate`
5. Install dependencies: `pip install -e .` or `pip install -r requirements` 