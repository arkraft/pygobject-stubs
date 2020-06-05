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


class Sequence(__gi.Struct):
    # no doc
    def append(self, data=None): # real signature unknown; restored from __doc__
        """ append(self, data=None) -> GLib.SequenceIter """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get(self, iter): # real signature unknown; restored from __doc__
        """ get(iter:GLib.SequenceIter) """
        pass

    def get_begin_iter(self): # real signature unknown; restored from __doc__
        """ get_begin_iter(self) -> GLib.SequenceIter """
        pass

    def get_end_iter(self): # real signature unknown; restored from __doc__
        """ get_end_iter(self) -> GLib.SequenceIter """
        pass

    def get_iter_at_pos(self, pos): # real signature unknown; restored from __doc__
        """ get_iter_at_pos(self, pos:int) -> GLib.SequenceIter """
        pass

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def insert_before(self, iter, data=None): # real signature unknown; restored from __doc__
        """ insert_before(iter:GLib.SequenceIter, data=None) -> GLib.SequenceIter """
        pass

    def is_empty(self): # real signature unknown; restored from __doc__
        """ is_empty(self) -> bool """
        return False

    def move(self, src, dest): # real signature unknown; restored from __doc__
        """ move(src:GLib.SequenceIter, dest:GLib.SequenceIter) """
        pass

    def move_range(self, dest, begin, end): # real signature unknown; restored from __doc__
        """ move_range(dest:GLib.SequenceIter, begin:GLib.SequenceIter, end:GLib.SequenceIter) """
        pass

    def prepend(self, data=None): # real signature unknown; restored from __doc__
        """ prepend(self, data=None) -> GLib.SequenceIter """
        pass

    def range_get_midpoint(self, begin, end): # real signature unknown; restored from __doc__
        """ range_get_midpoint(begin:GLib.SequenceIter, end:GLib.SequenceIter) -> GLib.SequenceIter """
        pass

    def remove(self, iter): # real signature unknown; restored from __doc__
        """ remove(iter:GLib.SequenceIter) """
        pass

    def remove_range(self, begin, end): # real signature unknown; restored from __doc__
        """ remove_range(begin:GLib.SequenceIter, end:GLib.SequenceIter) """
        pass

    def set(self, iter, data=None): # real signature unknown; restored from __doc__
        """ set(iter:GLib.SequenceIter, data=None) """
        pass

    def swap(self, a, b): # real signature unknown; restored from __doc__
        """ swap(a:GLib.SequenceIter, b:GLib.SequenceIter) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Sequence), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Sequence' objects>, '__weakref__': <attribute '__weakref__' of 'Sequence' objects>, '__doc__': None, 'append': gi.FunctionInfo(append), 'free': gi.FunctionInfo(free), 'get_begin_iter': gi.FunctionInfo(get_begin_iter), 'get_end_iter': gi.FunctionInfo(get_end_iter), 'get_iter_at_pos': gi.FunctionInfo(get_iter_at_pos), 'get_length': gi.FunctionInfo(get_length), 'is_empty': gi.FunctionInfo(is_empty), 'prepend': gi.FunctionInfo(prepend), 'get': gi.FunctionInfo(get), 'insert_before': gi.FunctionInfo(insert_before), 'move': gi.FunctionInfo(move), 'move_range': gi.FunctionInfo(move_range), 'range_get_midpoint': gi.FunctionInfo(range_get_midpoint), 'remove': gi.FunctionInfo(remove), 'remove_range': gi.FunctionInfo(remove_range), 'set': gi.FunctionInfo(set), 'swap': gi.FunctionInfo(swap)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Sequence)


