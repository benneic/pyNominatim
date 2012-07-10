import datetime

def kwargs_converter(kwargs):
    return {key:param_converter(val) for key, val in kwargs.items() if val is not None}

def param_converter(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat() + 'Z'
    elif hasattr(obj, 'isoformat'):
        return obj.isoformat()
    elif obj is True:
        return 1
    elif obj is False:
        return 0
    else:
        return obj