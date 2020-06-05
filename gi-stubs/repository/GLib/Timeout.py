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


class Timeout(__gi_overrides_GLib.Source):
    """
    :Constructors:
    
    ::
    
        Source()
        new(source_funcs:GLib.SourceFuncs, struct_size:int) -> GLib.Source
    """
    def add_child_source(self, child_source): # real signature unknown; restored from __doc__
        """ add_child_source(self, child_source:GLib.Source) """
        pass

    def add_poll(self, fd): # real signature unknown; restored from __doc__
        """ add_poll(self, fd:GLib.PollFD) """
        pass

    def add_unix_fd(self, fd, events): # real signature unknown; restored from __doc__
        """ add_unix_fd(self, fd:int, events:GLib.IOCondition) """
        pass

    def attach(self, context=None): # real signature unknown; restored from __doc__
        """ attach(self, context:GLib.MainContext=None) -> int """
        return 0

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def get_can_recurse(self): # real signature unknown; restored from __doc__
        """ get_can_recurse(self) -> bool """
        return False

    def get_context(self): # real signature unknown; restored from __doc__
        """ get_context(self) -> GLib.MainContext or None """
        pass

    def get_current_time(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_ready_time(self): # real signature unknown; restored from __doc__
        """ get_ready_time(self) -> int """
        return 0

    def get_time(self): # real signature unknown; restored from __doc__
        """ get_time(self) -> int """
        return 0

    def is_destroyed(self): # real signature unknown; restored from __doc__
        """ is_destroyed(self) -> bool """
        return False

    def modify_unix_fd(self, tag, new_events): # real signature unknown; restored from __doc__
        """ modify_unix_fd(self, tag, new_events:GLib.IOCondition) """
        pass

    def new(self, source_funcs, struct_size): # real signature unknown; restored from __doc__
        """ new(source_funcs:GLib.SourceFuncs, struct_size:int) -> GLib.Source """
        pass

    def query_unix_fd(self, tag): # real signature unknown; restored from __doc__
        """ query_unix_fd(self, tag) -> GLib.IOCondition """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.Source """
        pass

    def remove(self, tag): # real signature unknown; restored from __doc__
        """ remove(tag:int) -> bool """
        return False

    def remove_by_funcs_user_data(self, funcs, user_data=None): # real signature unknown; restored from __doc__
        """ remove_by_funcs_user_data(funcs:GLib.SourceFuncs, user_data=None) -> bool """
        return False

    def remove_by_user_data(self, user_data=None): # real signature unknown; restored from __doc__
        """ remove_by_user_data(user_data=None) -> bool """
        return False

    def remove_child_source(self, child_source): # real signature unknown; restored from __doc__
        """ remove_child_source(self, child_source:GLib.Source) """
        pass

    def remove_poll(self, fd): # real signature unknown; restored from __doc__
        """ remove_poll(self, fd:GLib.PollFD) """
        pass

    def remove_unix_fd(self, tag): # real signature unknown; restored from __doc__
        """ remove_unix_fd(self, tag) """
        pass

    def set_callback(self, fn, user_data=None): # reliably restored by inspect
        # no doc
        pass

    def set_callback_indirect(self, callback_data=None, callback_funcs): # real signature unknown; restored from __doc__
        """ set_callback_indirect(self, callback_data=None, callback_funcs:GLib.SourceCallbackFuncs) """
        pass

    def set_can_recurse(self, can_recurse): # real signature unknown; restored from __doc__
        """ set_can_recurse(self, can_recurse:bool) """
        pass

    def set_funcs(self, funcs): # real signature unknown; restored from __doc__
        """ set_funcs(self, funcs:GLib.SourceFuncs) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_name_by_id(self, tag, name): # real signature unknown; restored from __doc__
        """ set_name_by_id(tag:int, name:str) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
        pass

    def set_ready_time(self, ready_time): # real signature unknown; restored from __doc__
        """ set_ready_time(self, ready_time:int) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def _Source__get_can_recurse(self): # reliably restored by inspect
        # no doc
        pass

    def _Source__get_priority(self): # reliably restored by inspect
        # no doc
        pass

    def _Source__set_can_recurse(self, value): # reliably restored by inspect
        # no doc
        pass

    def _Source__set_priority(self, value): # reliably restored by inspect
        # no doc
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __del__(self): # reliably restored by inspect
        # no doc
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

    def __init__(self, interval=0, priority=0): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, interval=0, priority=0): # reliably restored by inspect
        # no doc
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

    callback_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    callback_funcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_recurse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poll_fds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_funcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.GLib', '__new__': <staticmethod object at 0x7f1d2ccaa760>, '__init__': <function Timeout.__init__ at 0x7f1d2ccc7310>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType GSource (94243598374464)>'
    __info__ = StructInfo(Source)


