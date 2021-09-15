class TestBlueprintSurvivorCount:
    """
    Test the survivor count blueprint
    """

    def test_invalid_data_format(self, api):
        """
        GIVEN the endpoint is called
        WHEN the data payload is of the incorrect format
        THEN return a 400 response
        """
        with api:
            res = api.post('/survivorCount',
                           json={},
                           headers={'Content-Type': 'application/json'})
            assert res.status_code == 400
            assert res.json['message'] == 'BadRequest'

    def test_invalid_field_type(self, api):
        """
        GIVEN the endpoint is called
        WHEN when the bin field is not of type integer
        THEN return a 404 response
        """
        with api:
            res = api.post('/survivorCount',
                           json={},
                           headers={'Content-Type': 'application/json'})
            assert res.status_code == 404
            assert res.json['message'] == 'NotFound'

    def test_valid_data_format(self, api):
        """
        GIVEN the endpoint is called
        WHEN the data payload is of the correct format
        THEN return 200 with the survivor count
        """
        with api:
            res = api.post('/survivorCount',
                           json={},
                           headers={'Content-Type': 'application/json'})
            assert res.status_code == 200
            assert res.json['message'] == 'survivors counted successfully'
