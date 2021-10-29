
from argparse import Action, ArgumentParser


def DriverAction(Action):
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
        help="URL of the database to backup"
    )
    parser.add_argument(
        "--driver",
        nargs=2,
        action=DriverAction,
        required=True,
        help="How and where to store the backup",

    )
    return parser  