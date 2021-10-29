
def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()


def s3(client, infile, bucket, name):
    """
    client: An AWS client object that has an upload_fileobj method.
    infile: A file object with the data from our PostgreSQL backup.
    bucket: The name of the bucket that we'll be storing the backup in.
    name: The name of the file we'd like to create in our S3 bucket.
    """
    client.upload_fileobj(infile, bucket, name)


    """(pgbackup) $ echo "UPLOADED" > example.txt
    (pgbackup) $ PYTHONPATH=./src python
    >>> import boto3
    >>> from pgbackup import storage
    >>> client = boto3.client('s3')
    >>> infile = open('example.txt', 'rb')
    >>> storage.s3(client, infile, 'backupdb-bucket', infile.name)
    """