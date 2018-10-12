
import os , tempfile, pytest

import app

from flask import url_for

@pytest.fixture
def app():
    app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

def test_landing(client):
    assert client.get(url_for('/')).status_code == 200