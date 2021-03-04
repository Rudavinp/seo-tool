import sys
# from app import  app


def test_home_page(client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the respons is valid
    :param test_client:
    :return:
    """

    response = client.get('/')
    assert response.status_code == 200
    assert b'Easy_seo' in response.data
    assert b'Easy' in response.data


def test_start_page(client):
    """
    GIVEN a Flask application
    WHEN the '/start' page is requested (POST)
    THEN check the respons is valid
    :param client:
    :return:
    """

    response = client.post('/start', data=b'{"text": "lol"}')
    assert response.status_code == 200


def test_result_page(client):
    """
    GIVEN a Flask application
    WHEN the '/result' page is requested (GET)
    THEN check the respons is valid
    :param client:
    :return:
    """

    response = client.get('/results/1')
    assert response.status_code == 200
