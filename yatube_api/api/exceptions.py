from rest_framework.exceptions import APIException


class CustomValidationError(APIException):
    status_code = 400
    default_detail = 'Validation error'
    default_code = 'bad_request'
