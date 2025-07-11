# -*- encoding: utf-8 -*-

from pathlib import Path

import yaml


class Config():
    def __init__(self):
        self.path_config = PathConfig()
        self.fonts_config = FontsConfig(path_config=self.path_config)
        self.locales_config = LocalesConfig()


# ---------------------------------------------------------
# Fonts
# ---------------------------------------------------------

class FontsConfig():
    def __init__(self, *, path_config):
        self.fonts_path = path_config.externals_path.joinpath('fonts')

        config_path = path_config.config_path.joinpath('fonts.yml')
        with open(config_path, 'r', encoding='utf-8') as fp:
            self._fonts = yaml.full_load(fp)

    def by_locale(self, locale):
        if locale not in self._fonts:
            raise RuntimeError('Not supported locale. :: locale={}'.format(locale))
        return self._fonts[locale]


# ---------------------------------------------------------
# Path
# ---------------------------------------------------------

class PathConfig():
    def __init__(self):
        self.root_path = Path(__file__).resolve().parents[2]
        self.externals_path = self.root_path.joinpath('externals')
        self.project_path = Path(__file__).resolve().parents[1]
        self.config_path = self.project_path.joinpath('config').resolve()


# ---------------------------------------------------------
# Locales
# ---------------------------------------------------------

class LocalesConfig():
    @property
    def locales(self):
        return ['ja', 'ko', 'zh-Hans', 'zh-Hant', 'en']
