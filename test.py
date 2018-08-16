
import os , tempfile, pytest

import app

@pytest.fixture
def client():
    app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    