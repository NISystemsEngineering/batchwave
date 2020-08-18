import functools


def constrain_type(required_type: type, position=1):
    def wrapper(func):
        @functools.wraps(func)
        def set_value(*args, **kwargs):
            if not isinstance(args[position], required_type):
                raise TypeError('Value must be instance of type ' + str(required_type))
            func(*args, **kwargs)
        return set_value
    return wrapper
