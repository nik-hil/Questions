# https://stackoverflow.com/a/6798042/618018

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    pass

# class Logger(object):
#     __metaclass__ = Singleton


print(id(Logger()), id(Logger()))
