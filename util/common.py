# coding=utf-8


class DictObj(dict):
    """A dict that allows for object-like property access syntax."""

    def __init__(self, *args, **kwargs):
        super(DictObj, self).__init__(*args, **kwargs)
        for k, v in args[0].items():
            if type(v) == dict:
                self[k] = DictObj(v)
            elif type(v) == list:
                self[k] = [DictObj(value) if type(value) == dict else value for value in v]

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            return None

    def __setattr__(self, key, value):
        self[key] = value


def get_string(content, default_value=""):
    if content is None:
        return default_value
    return content


def not_none_number(content, default_value=0):
    if content is None:
        return default_value
    return content
