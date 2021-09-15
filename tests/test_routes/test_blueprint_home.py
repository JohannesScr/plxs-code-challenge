class TestBlueprintHome:
    """
    Test the home blueprint
    """
    def test_home(self, api):
        """
        GIVEN the API home route is called
        THEN return a generic response
        """
        with api:
            res = api.get('/')
            assert res.status_code == 200
            assert res.json['message'] == 'Welcome to this server'
