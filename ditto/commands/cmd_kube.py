import click


@click.group('kube')
def cli():
    """Kubernetes cluster commands"""
    pass


@cli.command('init')
def kube_init():
    pass


@cli.command('update')
def kube_init():
    pass


@cli.command('nuke')
def kube_nuke():
    pass

