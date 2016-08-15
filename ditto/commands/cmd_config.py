import click
from ditto.core import logger, config


@click.group('config')
def cli():
    """Configuration commands"""
    pass


@cli.command('set')
@click.option('--key', prompt=True)
@click.option('--value', prompt=True)
def config_set(key, value):
    c = config.DittoConfig()
    c.set(key, value)


@cli.command('get')
@click.option('--key', prompt=True)
def config_get(key):
    c = config.DittoConfig()
    logger.log(c.get(key))


@cli.command('rm')
@click.option('--key', prompt=True)
def config_rm(key):
    c = config.DittoConfig()
    c.rm(key)


@cli.command('ls')
def config_ls():
    c = config.DittoConfig()
    c.list()
