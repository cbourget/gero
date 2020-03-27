import fire

from gero.app import create_app
from gero.cli.context import create_cli_context

CLI_HANDLER = 'clihandler'


def main():
    app = create_app({})
    app.include('gero.cli.handlers')
    context = create_cli_context(app)
    fire.Fire({
        '.'.join(token[1:]): handler
        for handler, token in context.get_instance(CLI_HANDLER, many=True)
        if handler is not None  
    })
