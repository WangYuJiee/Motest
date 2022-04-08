# -*- coding: utf-8 -*-#
"""
    @Name: local_storage 
    @Author:  49173
    @Date:  2022-04-08
    @Description: from werkzeug import local
"""
try:
    from greenlet import getcurrent as _get_ident
except ImportError:
    try:
        from thread import get_ident as _get_ident
    except ImportError:
        from _thread import get_ident  as _get_ident


class Local(object):
    __slots__ = ('__storage__', '__ident_func__')

    def __init__(self):
        object.__setattr__(self, '__storage__', {})
        object.__setattr__(self, '__ident_func__', _get_ident)

    def __iter__(self):
        return iter(self.__storage__.items())

    def __release_local__(self):
        self.__storage__.pop(self.__ident_func__(), None)

    def __getattr__(self, name):
        return self.__storage__[self.__ident_func__()][name]

    def __setattr__(self, name, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}

    def __delattr__(self, name):
        try:
            del self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)


local_data = Local()