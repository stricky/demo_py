from source.API.api import API, Session
from pytest import fixture


@fixture
def api():
    api = API(Session('https://mockaroo.com/'))
    return api
