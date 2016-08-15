import atexit
import logging
import os
import sys

import click
from core import util, logger, context

pass_context = click.make_pass_decorator(context.DittoContext, ensure=True)
cmd_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))


class Ditto(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []

        for filename in os.listdir(cmd_dir):
            if filename.endswith('.py') and filename.startswith('cmd_'):
                rv.append(filename[4:-3])

        rv.sort()
        return rv

    def get_command(self, ctx, cmd_name):
        ns = {}
        fn = os.path.join(cmd_dir, 'cmd_' + cmd_name + '.py')

        if os.path.isfile(fn):
            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                eval(code, ns, ns)
            return ns['cli']
        else:
            sys.exit("Error: Plugin " + cmd_name + " not found!")


@click.command(cls=Ditto, context_settings=dict(auto_envvar_prefix='DITTO'))
@click.option('-v', '--verbose', is_flag=True)
@pass_context
def cli(ctx, verbose):
    """Ditto - !"""
    ditto_log = logger.setup()
    ctx.start_clock()
    ditto_log.propagate=False

    if verbose:
        ditto_log.setLevel(logging.DEBUG)
    else:
        ditto_log.setLevel(logging.INFO)

    if not util.is_admin_shell():
        logger.vlog("Script run without admin privileges")

    atexit.register(context.DittoContext.stop_clock, ctx)

