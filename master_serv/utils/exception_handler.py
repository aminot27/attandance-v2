from rest_framework.views import exception_handler

from master_serv.utils.error_response import ErrorResponse


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    # print("-----------exc----------")
    # print(exc)
    # print(exc.__class__)
    # print("-----------context----------")
    # print(context)
    response = exception_handler(exc, context)
    # print("-----------response----------")
    # print(response.data)
    handlers = {
        'ValidationError': handle_validation_error,
        'NotFound': handle_not_found_error,
        'MethodNotAllowed': handle_method_not_allowed,
        'APIException': handle_generic_error
    }
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response


def handle_generic_error(exc, context, response):
    return ErrorResponse(details_=response.data['detail'], path_=context['request'].path).send_internal_server_error()


def handle_validation_error(exc, context, response):
    return ErrorResponse(details_=response.data, path_=context['request'].path).send_bad_request()


def handle_not_found_error(exc, context, response):
    return ErrorResponse(details_=response.data["detail"], path_=context['request'].path).send_not_found()


def handle_method_not_allowed(exc, context, response):
    return ErrorResponse(msg_=context['request'].method, path_=context['request'].path).send_method_not_allowed()
