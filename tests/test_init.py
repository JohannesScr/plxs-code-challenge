from src.app.config import get_config


class TestInit:
    """
    Test the initialisation of the server
    """

    def test_home(self, api):
        """
        GIVEN the server is started
        WHEN the home route is hit
        THEN return a json object with a welcome message
        """
        with api:
            res = api.get('/')
            assert res.status_code == 200


class TestGetConfig:

    def test_invalid_env_file(self):
        """
        GIVEN the environmental variables are to be fetched
        WHEN the env file name is invalid or not existing
        THEN it should return an empty Config object
        """
        c = get_config(env='')
        assert isinstance(c, object)
        assert hasattr(c, 'ENV') is False

    def test_valid_env_file(self):
        """
        GIVEN the environmental variables are to be fetched
        WHEN the function is called
        THEN it should load the env vars and return a object containing
            the vars
        """
        c = get_config(env='.env')
        assert hasattr(c, 'ENV')
        assert c.ENV == 'development'
