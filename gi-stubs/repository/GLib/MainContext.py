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


from .MainContext import MainContext

class MainContext(MainContext):
    """
    :Constructors:
    
    ::
    
        new() -> GLib.MainContext
    """
    def acquire(self): # real signature unknown; restored from __doc__
        """ acquire(self) -> bool """
        return False

    def add_poll(self, fd, priority): # real signature unknown; restored from __doc__
        """ add_poll(self, fd:GLib.PollFD, priority:int) """
        pass

    def check(self, max_priority, fds): # real signature unknown; restored from __doc__
        """ check(self, max_priority:int, fds:list) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def default(self): # real signature unknown; restored from __doc__
        """ default() -> GLib.MainContext """
        pass

    def dispatch(self): # real signature unknown; restored from __doc__
        """ dispatch(self) """
        pass

    def find_source_by_funcs_user_data(self, funcs, user_data=None): # real signature unknown; restored from __doc__
        """ find_source_by_funcs_user_data(self, funcs:GLib.SourceFuncs, user_data=None) -> GLib.Source """
        pass

    def find_source_by_id(self, source_id): # real signature unknown; restored from __doc__
        """ find_source_by_id(self, source_id:int) -> GLib.Source """
        pass

    def find_source_by_user_data(self, user_data=None): # real signature unknown; restored from __doc__
        """ find_source_by_user_data(self, user_data=None) -> GLib.Source """
        pass

    def get_thread_default(self): # real signature unknown; restored from __doc__
        """ get_thread_default() -> GLib.MainContext """
        pass

    def invoke_full(self, priority, function, data=None): # real signature unknown; restored from __doc__
        """ invoke_full(self, priority:int, function:GLib.SourceFunc, data=None) """
        pass

    def is_owner(self): # real signature unknown; restored from __doc__
        """ is_owner(self) -> bool """
        return False

    def iteration(self, may_block=True): # reliably restored by inspect
        # no doc
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GLib.MainContext """
        pass

    def pending(self): # real signature unknown; restored from __doc__
        """ pending(self) -> bool """
        return False

    def pop_thread_default(self): # real signature unknown; restored from __doc__
        """ pop_thread_default(self) """
        pass

    def prepare(self): # real signature unknown; restored from __doc__
        """ prepare(self) -> bool, priority:int """
        return False

    def push_thread_default(self): # real signature unknown; restored from __doc__
        """ push_thread_default(self) """
        pass

    def query(self, max_priority): # real signature unknown; restored from __doc__
        """ query(self, max_priority:int) -> int, timeout_:int, fds:list """
        return 0

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.MainContext """
        pass

    def ref_thread_default(self): # real signature unknown; restored from __doc__
        """ ref_thread_default() -> GLib.MainContext """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def remove_poll(self, fd): # real signature unknown; restored from __doc__
        """ remove_poll(self, fd:GLib.PollFD) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def wait(self, cond, mutex): # real signature unknown; restored from __doc__
        """ wait(self, cond:GLib.Cond, mutex:GLib.Mutex) -> bool """
        return False

    def wakeup(self): # real signature unknown; restored from __doc__
        """ wakeup(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> GLib.MainContext """
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.GLib', 'iteration': <function MainContext.iteration at 0x7f8514879310>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType GMainContext (94581033130992)>'
    __info__ = StructInfo(MainContext)


