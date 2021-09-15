from logging import getLogger

log = getLogger(__name__)


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
            payload = {}
            res = api.post('/survivorCount',
                           json=payload,
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
            payload = {
                'data': [
                    {
                        'PassengerId': 1,
                        'Survived': 1,
                        'Pclass': 12,
                        'Name': 'james',
                        'Sex': 'male',
                        'Age': 23,
                        'SibSp': 1,
                        'Parch': 0,
                        'Ticket': 'A/521171'
                    }
                ],
                'binField': 'Name',
                'binBoundaries': [5, 10]
            }
            res = api.post('/survivorCount',
                           json=payload,
                           headers={'Content-Type': 'application/json'})
            log.info(res.json)
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
