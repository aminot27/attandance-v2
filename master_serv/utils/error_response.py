from rest_framework.response import Response
from rest_framework import status


class ErrorResponse:
    """
    An error HttpResponse class that send error responses information.
    """

    def __init__(self, data_=None, msg_="BAD REQUEST", details_=None, path_=""):
        self.data = data_
        self.msg = msg_
        self.details = details_
        self.path = path_
        self.result = {
            'data': data_,
            'message': msg_,
            'details': details_,
            'path': path_,
            "status": False,
        }

    def send_bad_request(self):
        self.result['message'] = self.msg
        return Response(self.result, status=status.HTTP_400_BAD_REQUEST)

    def send_unauthorized(self):
        self.result['message'] = "UNAUTHORIZED ACCESS"
        return Response(self.result, status=status.HTTP_401_UNAUTHORIZED)

    def send_forbidden(self):
        self.result['message'] = "FORBIDDEN ACCESS"
        return Response(self.result, status=status.HTTP_403_FORBIDDEN)

    def send_not_found(self):
        if self.msg == "BAD REQUEST":
            self.result['message'] = "REGISTER NOT_FOUND"
        return Response(self.result, status=status.HTTP_404_NOT_FOUND)

    def send_internal_server_error(self):
        self.result['message'] = "INTERNAL SERVER ERROR"
        return Response(self.result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def send_validation_error(self):
        self.result['message'] = "ERROR VALIDATING FIELDS"
        return Response(self.result, status=status.HTTP_400_BAD_REQUEST)

    def send_method_not_allowed(self):
        self.result['message'] = "METHOD " + self.msg + " NOT ALLOWED"
        return Response(self.result, status=status.HTTP_405_METHOD_NOT_ALLOWED)
