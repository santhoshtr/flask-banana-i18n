#  Copyright (C) 2020  Kunal Mehta <legoktm@member.fsf.org>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from typing import Optional

from banana_i18n import BananaI18n
from flask import Flask, current_app
try:
    from flask_uls import ULS
except ImportError:
    ULS = None  # type: ignore


class Banana:
    def __init__(self, app=None, messagesdir=None, uls=None):
        self.banana = None  # type: Optional[BananaI18n]
        self.uls = None  # type: Optional[ULS]
        self._language = None
        if app is not None:
            self.init_app(app, messagesdir, uls)

    def init_app(self, app: Flask, messagesdir, uls: Optional[ULS] = None):
        app.config.setdefault('BANANA_DEFAULT_LANGUAGE', 'en')
        self.banana = BananaI18n(messagesdir)
        self.uls = uls
        if self.uls is not None:
            app.config['ULS_ENABLED_LANGUAGES'] = self.banana.known_languages()

        @app.context_processor
        def inject_to_templates() -> dict:
            return {
                '_': self.translate,
            }

    @property
    def language(self) -> str:
        if self._language is not None:
            # Manually overridden
            return self._language
        if self.uls is not None:
            # Defer to ULS
            return self.uls.language
        # Hardcoded fallback
        return current_app.config['BANANA_DEFAULT_LANGUAGE']

    @language.setter
    def language(self, lang: str):
        # TODO: validation
        self._language = lang

    def translate(self, *args, **kwargs):
        """proxy method with correct language"""
        # TODO: implement qqx
        return self.banana.translate(self.language, *args, **kwargs)
