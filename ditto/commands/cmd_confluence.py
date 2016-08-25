import click
from ditto.core import config, util, confluence_client


@click.group('confluence')
def cli():
    """Confluence commands"""
    pass


@cli.command('update_page')
@click.option('--url', prompt=config.not_set("confluence.url"), default=config.get("confluence.url"))
@click.option('--username', prompt=config.not_set("confluence.username"), default=config.get("confluence.username"))
@click.option('--password', prompt=config.not_set("confluence.password"), default=config.get("confluence.password"), hide_input=True, confirmation_prompt=False)
@click.option('--space', prompt=True)
@click.option('--page', prompt=True)
@click.option('--html_file', prompt=True, type=click.Path(exists=True))
def confluence_update(url, username, password, space, page, html_file):
    conf_client = confluence_client.ConfluenceClient(url, username, password)

    page_id = conf_client.get_page_id(space, page)
    page_data = conf_client.page(page_id)
    version = page_data['version']['number'] + 1

    html = util.read_file_to_str(html_file)
    conf_client.save_content(page_id, version, page, html)


@cli.command('create_page')
@click.option('--url', prompt=config.not_set("confluence.url"), default=config.get("confluence.url"))
@click.option('--username', prompt=config.not_set("confluence.username"), default=config.get("confluence.username"))
@click.option('--password', prompt=config.not_set("confluence.password"), default=config.get("confluence.password"), hide_input=True, confirmation_prompt=False)
@click.option('--space', prompt=True)
@click.option('--parent_page', prompt=True)
@click.option('--page', prompt=True)
@click.option('--html_file', prompt=True, type=click.Path(exists=True))
def confluence_create(url, username, password, space, parent_page, page, html_file):
    conf_client = confluence_client.ConfluenceClient(url, username, password)
    page_id = conf_client.get_page_id(space, parent_page)
    html = util.read_file_to_str(html_file)
    conf_client.new_child_page(page_id, space, page, html)
