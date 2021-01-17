from django.core.exceptions import ValidationError

def validate_code(value):
    if len(value)<3:
        msg = u"너무짧음"
        raise ValidationError(msg)