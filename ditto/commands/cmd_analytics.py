import click
from ditto.core import util, config

from ditto.ditto import pass_context


@click.group('analytics')
def cli():
    """Analytics Commands"""
    pass


# @cli.command('config')
# def analytics_config(enabled, url, type, url, username, password):
#     pass

@cli.command('on')
def analytics_on():
    config.set("analytics.enabled", "Y")


@cli.command('off')
def analytics_off():
    config.set("analytics.enabled", "N")


@cli.command('submit')
@click.option('--json', default="{}")
@click.option('--key', default='general')
@pass_context
def analytics_submit(ctx, key, json):
    json_data = util.read_json_str(json)
    ctx.analytics_service.add_metric(key, json_data)
