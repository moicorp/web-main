# -*- encoding: utf-8 -*-

import asyncio
import os
from pathlib import Path
from aiohttp.web import Application

from config import Config
from context_holder import ContextHolder
from locales import Locales
from web import controllers

from emoji.config import load_config


class Context():
    @classmethod
    async def get_context(cls):
        if ContextHolder.context is None:
            context = Context()
            await context.startup()
            ContextHolder.set_context(context)
        return ContextHolder.context


    def __init__(self):
        is_dev = os.getenv('PYTHON_ENV') != 'production'
        app = Application(debug=is_dev)
        app['config'] = load_config()

        self._config = Config()
        self._locales = Locales(self._config.locales_config)
        self.app = app


    async def startup(self):
        controllers.startup(self.app)

    @property
    def config(self):
        return self._config

    @property
    def locales(self):
        return self._locales
