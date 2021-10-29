
from argparse import Action, ArgumentParser
from os import pardir


class DriverAction(Action):
    """
    Namespace is a class that stores the arguments passed in the CLI.
    collect driver & destination from values and store them in the namespace
    using the dot notation appropriately
    """
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = ArgumentParser(description="""
    Back up PostgreSQl databases Locally or to AWS S3
    """
    )
    parser.add_argument(
        "url", 
        help="URL of the database you want to perform the backup"
    )
    parser.add_argument(
        "--driver", '-d',
        nargs=2,
        action=DriverAction,
        required=True,
        metavar=("DRIVER", "DESTINATION"),
        help="How and where to store the backup",
    )
    return parser  


def main():
    import boto3
    import time
    from backupdb import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_filename(args.url, timestamp)
        print(f"Backing {file_name} Database up into {args.destination} bucket in S3")
        storage.s3(client, dump.stdout, args.destination, file_name)
        print("Backup successful!")
    else:
        with open(args.destination, 'wb') as outfile:
            print(f"Backing Database up locally to {outfile.name}")
            storage.local(dump.stdout, outfile)
            print("Backup Successful!")