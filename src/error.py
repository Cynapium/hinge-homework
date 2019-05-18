
class ResponseStatus:
    OK = 200
    BAD_REQUEST = 400       # Client error
    SERVER_ERROR = 500

class SuccessResponse:

    def __init__(detail):
        self.status = 

class ErrorResponse:

    def __init__(self, status, detail):
        self.status = status
        self.detail = detail
