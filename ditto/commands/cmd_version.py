import click
from ditto.core import util, logger


@click.command('version')
def cli():
    """"""
    logger.log("Ditto Version " + util.ditto_version())
    logger.log("Installed at " + util.ditto_dir())
