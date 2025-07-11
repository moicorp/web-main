# -*- encoding: utf-8 -*-

from pathlib import Path

from web.controllers import emoji
from web.controllers.emoji import download, generate
from web.controllers.healthcheck import ok


def startup(app):
    _setup_routes(app)
    _setup_static_routes(app)


def _setup_routes(app):
    app.router.add_get('/healthcheck', ok)
    app.router.add_get('/emoji', emoji.generate)
    app.router.add_get('/emoji_download', emoji.download)
    app.router.add_get('/img', emoji.view)


def _setup_static_routes(app):
    app.router.add_static(
        '/assets',
        str(Path(app['config']['project_path']).joinpath('assets')),
        name='static',
        append_version=True,
    )
