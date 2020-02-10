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

import pytest

from flask import Flask, render_template
from flask_banana import Banana
from pathlib import Path


@pytest.fixture()
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    banana = Banana(app, Path(__file__).resolve().parent / 'i18n')

    @app.route('/language')
    def language():
        return banana.language

    @app.route('/templates')
    def templates():
        return render_template('test.html')

    with app.test_client() as client:
        # So we can access it in test functions
        client.banana = banana
        yield client


def test_language(client):
    resp = client.get('/language')
    assert resp.data.decode() == 'en'
    client.banana.language = 'de'
    resp = client.get('/language')
    assert resp.data.decode() == 'de'


@pytest.mark.parametrize('lang,expected', (
    ('en', 'English message, Parameter: bar'),
    ('de', 'German message, Parameter in German: bar'),
))
def test_templates(client, lang, expected):
    client.banana.language = lang
    resp = client.get('/templates')
    assert resp.data.decode() == expected
