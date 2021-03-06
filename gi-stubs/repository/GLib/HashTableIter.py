# encoding: utf-8
# module gi.repository.GLib
# from /usr/lib64/girepository-1.0/GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # /usr/lib64/python3.8/site-packages/gi/_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gobject as __gobject


class HashTableIter(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        HashTableIter()
    """
    def init(self, hash_table): # real signature unknown; restored from __doc__
        """ init(self, hash_table:dict) """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool, key, value """
        return False

    def remove(self): # real signature unknown; restored from __doc__
        """ remove(self) """
        pass

    def replace(self, value=None): # real signature unknown; restored from __doc__
        """ replace(self, value=None) """
        pass

    def steal(self): # real signature unknown; restored from __doc__
        """ steal(self) """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    dummy1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(HashTableIter), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'HashTableIter' objects>, '__weakref__': <attribute '__weakref__' of 'HashTableIter' objects>, '__doc__': None, 'dummy1': <property object at 0x7f85134e1090>, 'dummy2': <property object at 0x7f85134e1180>, 'dummy3': <property object at 0x7f85134e1270>, 'dummy4': <property object at 0x7f85134e1360>, 'dummy5': <property object at 0x7f85134e1450>, 'dummy6': <property object at 0x7f85134e1540>, 'init': gi.FunctionInfo(init), 'next': gi.FunctionInfo(next), 'remove': gi.FunctionInfo(remove), 'replace': gi.FunctionInfo(replace), 'steal': gi.FunctionInfo(steal)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(HashTableIter)


