from src.includes.utils import Response


class TestResponse:
    """
    Test the Response Class
    """
    def test_default(self):
        """
        GIVEN a response is created
        WHEN no parameters are passed
        THEN return the default response of successful
        """
        res = Response().create()
        assert res.status_code == 200
        assert res.headers.get('Content-Type') == 'application/json'
        assert res.json['message'] == 'successful'
        assert res.json['data'] == {}
        assert res.json['errors'] == {}

    def test_valid_data(self):
        """
        GIVEN the response is created
        WHEN parameters are passed
        THEN return a response with those parameters
        """
        res = Response(http_code=403,
                       message='Unauthorised',
                       data={'survivors': 0}).create()
        assert res.status_code == 403
        assert res.headers.get('Content-Type') == 'application/json'
        assert res.json['message'] == 'Unauthorised'
        assert res.json['data'] == {'survivors': 0}
        assert res.json['errors'] == {}
