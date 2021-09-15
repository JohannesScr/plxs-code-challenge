import pytest
from src.app import create_server
from logging import getLogger

log = getLogger(__name__)


@pytest.fixture(scope='session')
def api():
    app = create_server(env='test')
    app.config.TESTING = True
    yield app.test_client()
    log.info('teardown API')
