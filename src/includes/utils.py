from flask import jsonify


class Response:
    def __init__(self,
                 http_code: int = None,
                 message: str = None,
                 data: dict = None,
                 errors: dict = None):
        self.status_code = http_code or 200
        self.message = message or 'successful'
        self.data = data or {}
        self.errors = errors or {}

    def create(self):
        resp = jsonify(message=self.message,
                       data=self.data,
                       errors=self.errors)
        resp.status_code = self.status_code
        resp.headers.add('Content-Type', 'application/json')
        return resp
