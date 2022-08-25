import os
import click


def register(app):
    @app.cli.group()
    def translate():
        """Команди перекладу та локалізації."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Ініціалізація нової мови."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system(
                'pybabel init -i messages.pot -d app/translations -l ' + lang):
            raise RuntimeError('init command failed')
        os.remove('messages.pot')

    @translate.command()
    def update():
        """Оновити всі мови."""
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('extract command failed')
        if os.system('pybabel update -i messages.pot -d app/translations'):
            raise RuntimeError('update command failed')
        os.remove('messages.pot')


    @translate.command()
    def compile():
        """Компілюйте всі мови."""
        if os.system('pybabel compile -d app/translations'):
            raise RuntimeError('compile command failed')

