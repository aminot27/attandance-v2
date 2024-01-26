from rest_framework.response import Response
from rest_framework import status


class SuccessResponse:
    """
    An success HttpResponse class that allows its data to be rendered into
    arbitrary media types.
    """

    def __init__(self, data_=None, msg_="Process executed successfully"):
        self.msg = msg_
        self.data = data_

    def send(self):
        result = {
            'data': self.data,
            'message': self.msg,
            "status": True,
        }
        return Response(result, status=status.HTTP_200_OK)

    def get_result(self):
        return {
            'data': self.data,
            'message': self.msg,
            "status": True,
        }
