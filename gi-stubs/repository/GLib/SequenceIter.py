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


class SequenceIter(__gi.Struct):
    # no doc
    def compare(self, b): # real signature unknown; restored from __doc__
        """ compare(self, b:GLib.SequenceIter) -> int """
        return 0

    def get_position(self): # real signature unknown; restored from __doc__
        """ get_position(self) -> int """
        return 0

    def get_sequence(self): # real signature unknown; restored from __doc__
        """ get_sequence(self) -> GLib.Sequence """
        pass

    def is_begin(self): # real signature unknown; restored from __doc__
        """ is_begin(self) -> bool """
        return False

    def is_end(self): # real signature unknown; restored from __doc__
        """ is_end(self) -> bool """
        return False

    def move(self, delta): # real signature unknown; restored from __doc__
        """ move(self, delta:int) -> GLib.SequenceIter """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> GLib.SequenceIter """
        pass

    def prev(self): # real signature unknown; restored from __doc__
        """ prev(self) -> GLib.SequenceIter """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SequenceIter), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'SequenceIter' objects>, '__weakref__': <attribute '__weakref__' of 'SequenceIter' objects>, '__doc__': None, 'compare': gi.FunctionInfo(compare), 'get_position': gi.FunctionInfo(get_position), 'get_sequence': gi.FunctionInfo(get_sequence), 'is_begin': gi.FunctionInfo(is_begin), 'is_end': gi.FunctionInfo(is_end), 'move': gi.FunctionInfo(move), 'next': gi.FunctionInfo(next), 'prev': gi.FunctionInfo(prev)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(SequenceIter)


