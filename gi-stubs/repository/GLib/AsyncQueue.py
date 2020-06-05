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


class AsyncQueue(__gi.Struct):
    # no doc
    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def length_unlocked(self): # real signature unknown; restored from __doc__
        """ length_unlocked(self) -> int """
        return 0

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) """
        pass

    def pop(self): # real signature unknown; restored from __doc__
        """ pop(self) """
        pass

    def pop_unlocked(self): # real signature unknown; restored from __doc__
        """ pop_unlocked(self) """
        pass

    def push(self, data=None): # real signature unknown; restored from __doc__
        """ push(self, data=None) """
        pass

    def push_front(self, item=None): # real signature unknown; restored from __doc__
        """ push_front(self, item=None) """
        pass

    def push_front_unlocked(self, item=None): # real signature unknown; restored from __doc__
        """ push_front_unlocked(self, item=None) """
        pass

    def push_unlocked(self, data=None): # real signature unknown; restored from __doc__
        """ push_unlocked(self, data=None) """
        pass

    def ref_unlocked(self): # real signature unknown; restored from __doc__
        """ ref_unlocked(self) """
        pass

    def remove(self, item=None): # real signature unknown; restored from __doc__
        """ remove(self, item=None) -> bool """
        return False

    def remove_unlocked(self, item=None): # real signature unknown; restored from __doc__
        """ remove_unlocked(self, item=None) -> bool """
        return False

    def timed_pop(self, end_time): # real signature unknown; restored from __doc__
        """ timed_pop(self, end_time:GLib.TimeVal) """
        pass

    def timed_pop_unlocked(self, end_time): # real signature unknown; restored from __doc__
        """ timed_pop_unlocked(self, end_time:GLib.TimeVal) """
        pass

    def timeout_pop(self, timeout): # real signature unknown; restored from __doc__
        """ timeout_pop(self, timeout:int) """
        pass

    def timeout_pop_unlocked(self, timeout): # real signature unknown; restored from __doc__
        """ timeout_pop_unlocked(self, timeout:int) """
        pass

    def try_pop(self): # real signature unknown; restored from __doc__
        """ try_pop(self) """
        pass

    def try_pop_unlocked(self): # real signature unknown; restored from __doc__
        """ try_pop_unlocked(self) """
        pass

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def unref_and_unlock(self): # real signature unknown; restored from __doc__
        """ unref_and_unlock(self) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AsyncQueue), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AsyncQueue' objects>, '__weakref__': <attribute '__weakref__' of 'AsyncQueue' objects>, '__doc__': None, 'length': gi.FunctionInfo(length), 'length_unlocked': gi.FunctionInfo(length_unlocked), 'lock': gi.FunctionInfo(lock), 'pop': gi.FunctionInfo(pop), 'pop_unlocked': gi.FunctionInfo(pop_unlocked), 'push': gi.FunctionInfo(push), 'push_front': gi.FunctionInfo(push_front), 'push_front_unlocked': gi.FunctionInfo(push_front_unlocked), 'push_unlocked': gi.FunctionInfo(push_unlocked), 'ref_unlocked': gi.FunctionInfo(ref_unlocked), 'remove': gi.FunctionInfo(remove), 'remove_unlocked': gi.FunctionInfo(remove_unlocked), 'timed_pop': gi.FunctionInfo(timed_pop), 'timed_pop_unlocked': gi.FunctionInfo(timed_pop_unlocked), 'timeout_pop': gi.FunctionInfo(timeout_pop), 'timeout_pop_unlocked': gi.FunctionInfo(timeout_pop_unlocked), 'try_pop': gi.FunctionInfo(try_pop), 'try_pop_unlocked': gi.FunctionInfo(try_pop_unlocked), 'unlock': gi.FunctionInfo(unlock), 'unref': gi.FunctionInfo(unref), 'unref_and_unlock': gi.FunctionInfo(unref_and_unlock)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AsyncQueue)


