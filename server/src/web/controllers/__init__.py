# -*- encoding: utf-8 -*-

from pathlib import Path

from web.controllers import emoji
from web.controllers.emoji import download, generate
from web.controllers.healthcheck import ok


def startup(app):
    _setup_routes(app)


def _setup_routes(app):
    app.router.add_get('/healthcheck', ok)
    app.router.add_get('/emoji', emoji.generate)
    app.router.add_get('/emoji_download', emoji.download)
    app.router.add_get('/img', emoji.view)
