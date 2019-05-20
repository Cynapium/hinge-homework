class Status:
    OK = 200
    BAD_REQUEST = 400       # Client error
    NOT_FOUND = 404
    SERVER_ERROR = 500

class ErrorResponse:

    def __init__(self, status, title, details=""):
        self.status = status
        self.title = title
        self.details = details

    def dump(self):
        return {
            "error": {
                "status": self.status,
                "title": self.title,
                "details": self.details
            }
        }, self.status

class ClientException(BaseException):
    pass
    
