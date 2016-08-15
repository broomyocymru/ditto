import click

from ditto.core import util


@click.group('docker')
def cli():
    """docker commands"""
    pass


@cli.command('nuke')
@click.option('--containers/--no-containers', default=True)
@click.option('--images/--no-images', default=True)
def docker_nuke(containers, images):
    if containers:
        util.shell_run("docker rm $(docker ps -a -q)")

    if images:
        util.shell_run("docker rmi $(docker images -q)")
