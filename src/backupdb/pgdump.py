
import subprocess
import sys


def dump(url):
    """pg_dump is PostgreSQL tool for backups of DBs. It takes a DB URL and
    build a list of tokens to build up the external command. subprocess.PIPE 
    to capture Stdount in a file-like object and prevent it from being written
    to the terminal when we run {{ pg_dump <url> }}"""
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)


def dump_filename(url, timestamp=None):
    db_name = url.split('/')[-1]
    db_name = db_name.split('?')[0]
    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db_name}.sql"

        

    """(pgbackup) $ PYTHONPATH=./src python
    >>> from pgbackup import pgdump
    >>> dump = pgdump.dump('postgres://postgres:password@54.245.63.9:80/
    sample')
    >>> f = open('dump.sql', 'w+b')
    >>> f.write(dump.stdout.read())
    >>> f.close()
    >>> exit()
    $ cat dump.sql
    """