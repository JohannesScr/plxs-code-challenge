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
