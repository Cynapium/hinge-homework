
class Status:
    OK = 200
    BAD_REQUEST = 400       # Client error
    NOT_FOUND = 404
    SERVER_ERROR = 500

class SuccessResponse:

    def __init__(self, details):
        self.status = Status.OK
        self.details = details

    def dump(self):
        return {
            "success": {
                "status": self.status,
                "details": self.details
            }
        }, self.status

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
