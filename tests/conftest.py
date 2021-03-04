import sys
import os
sys.path.append('/home/nio/py/2020/seo-tool')
print(sys.path)

import pytest
from easy_seo import app


from config import TestingConfig

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client



# @pytest.fixture(scope='module')
# def test_client():
#     app.config['TESTING'] = True
#
#     testing_client = flask_app.test_client()
#
#     ctx = flask_app.app_context()
#     ctx.push()
#
#     yield testing_client
#
#     ctx.pop()

