import click
from ditto.core import util, logger


@click.command('version')
def cli():
    """Print out Ditto details, use -v for licenses"""
    logger.log("Ditto Version " + util.ditto_version())
    logger.log("Installed at " + util.ditto_dir())

    logger.vlog("OSS Licenses:")
    logger.vjson(util.oss_licenses())

