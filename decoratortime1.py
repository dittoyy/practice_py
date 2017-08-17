#coding:utf-8
import time
from datetime import datetime
from datetime import timedelta


def timeguard(time_interval, default=None):
    def decorator(function):
        # For first time always run the function
        function.__last_run = datetime.min
        def guard(*args, **kwargs):
            now = datetime.now()
            if now - function.__last_run >= time_interval:
                function.__last_run = now
                return function(*args, **kwargs)
            elif default is not None:
                return default(*args, **kwargs)
        return guard
    return decorator


if __name__ == "__main__":

    @timeguard(timedelta(seconds=4),None)
    def add():
        print 12

    add()
    add()
    add()