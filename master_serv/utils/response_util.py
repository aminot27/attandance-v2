import datetime
import decimal
import json
from django.db.models import QuerySet, Model
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework import status


class DecimalJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal) or \
                isinstance(o, datetime.date) or \
                isinstance(o, datetime.time) or \
                isinstance(o, object):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)


class ToJson:
    def dict_json(self, d):
        """ compatible object django con json """
        d_ = {}
        for key in d:
            d_[key] = self.data_json(d[key])
        return d_

    def array_json(self, ar):
        """ compatible object django con json """
        ar_ = []
        for a in ar:
            ar_.append(self.data_json(a))
        return ar_

    def data_json(self, d):
        """ compatible object django con json """
        if isinstance(d, dict):
            return self.dict_json(d)
        elif isinstance(d, list):
            return self.array_json(d)
        elif isinstance(d, datetime.datetime):
            return json.dumps(d, cls=DecimalJSONEncoder)
        elif isinstance(d, datetime.date):
            return d.isoformat()
            # return json.dumps(d, cls=DecimalJSONEncoder)
        elif isinstance(d, decimal.Decimal):
            return float(d)
        elif isinstance(d, QuerySet):
            return self.array_json(list(d))
        elif isinstance(d, Model):
            return model_to_dict(d)
        else:
            return d


class Resp:
    """
    An HttpResponse class that allows its data to be rendered into
    arbitrary media types.
    """

    def __init__(self, data_=None, msg_="OK", status_=True, code_=200):
        self.status = status_
        self.msg = msg_
        self.data = data_
        self.code = code_

    def send(self):
        result = {
            'data': self.data,
            'message': self.msg,
            "status": self.status,
        }
        return Response(result, status=self.code)

    def result(self):
        return {
            'data': self.data,
            'message': self.msg,
            "status": self.status,
        }
