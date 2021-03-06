# encoding: utf-8
# module gi.repository.GObject
# from /usr/lib64/girepository-1.0/GObject-2.0.typelib
# by generator 1.147
# no doc

# imports
from gi.repository.GLib import (GError, IO_ERR, IO_FLAG_APPEND, 
    IO_FLAG_GET_MASK, IO_FLAG_IS_READABLE, IO_FLAG_IS_SEEKABLE, 
    IO_FLAG_IS_WRITEABLE, IO_FLAG_MASK, IO_FLAG_NONBLOCK, IO_FLAG_SET_MASK, 
    IO_HUP, IO_IN, IO_NVAL, IO_OUT, IO_PRI, IO_STATUS_AGAIN, IO_STATUS_EOF, 
    IO_STATUS_ERROR, IO_STATUS_NORMAL, OPTION_ERROR_BAD_VALUE, 
    OPTION_ERROR_FAILED, OPTION_ERROR_UNKNOWN_OPTION, OPTION_FLAG_FILENAME, 
    OPTION_FLAG_HIDDEN, OPTION_FLAG_IN_MAIN, OPTION_FLAG_NOALIAS, 
    OPTION_FLAG_NO_ARG, OPTION_FLAG_OPTIONAL_ARG, OPTION_FLAG_REVERSE, 
    SPAWN_CHILD_INHERITS_STDIN, SPAWN_DO_NOT_REAP_CHILD, 
    SPAWN_FILE_AND_ARGV_ZERO, SPAWN_LEAVE_DESCRIPTORS_OPEN, SPAWN_SEARCH_PATH, 
    SPAWN_STDERR_TO_DEV_NULL, SPAWN_STDOUT_TO_DEV_NULL, 
    filename_display_basename, filename_display_name, get_application_name, 
    get_prgname, main_context_default, main_depth, set_application_name, 
    set_prgname, source_remove, uri_list_extract_uris)

from gi._gi import (GObjectWeakRef, OptionContext, OptionGroup, Pid, 
    add_emission_hook, list_properties, new, signal_new, spawn_async, 
    type_register)

from gobject import (GBoxed, GEnum, GFlags, GInterface, GParamSpec, GPointer, 
    GType, Warning)

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GLib as __gi_repository_GLib
import gi._signalhelper as __gi__signalhelper
import gobject as __gobject


class ValueArray(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        ValueArray()
        new(n_prealloced:int) -> GObject.ValueArray
    """
    def append(self, value=None): # real signature unknown; restored from __doc__
        """ append(self, value:GObject.Value=None) -> GObject.ValueArray """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GObject.ValueArray """
        pass

    def get_nth(self, index_): # real signature unknown; restored from __doc__
        """ get_nth(self, index_:int) -> GObject.Value """
        pass

    def insert(self, index_, value=None): # real signature unknown; restored from __doc__
        """ insert(self, index_:int, value:GObject.Value=None) -> GObject.ValueArray """
        pass

    def new(self, n_prealloced): # real signature unknown; restored from __doc__
        """ new(n_prealloced:int) -> GObject.ValueArray """
        pass

    def prepend(self, value=None): # real signature unknown; restored from __doc__
        """ prepend(self, value:GObject.Value=None) -> GObject.ValueArray """
        pass

    def remove(self, index_): # real signature unknown; restored from __doc__
        """ remove(self, index_:int) -> GObject.ValueArray """
        pass

    def sort(self, compare_func, user_data=None): # real signature unknown; restored from __doc__
        """ sort(self, compare_func:GLib.CompareDataFunc, user_data=None) -> GObject.ValueArray """
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

    n_prealloced = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ValueArray), '__module__': 'gi.repository.GObject', '__gtype__': <GType GValueArray (94184341423200)>, '__dict__': <attribute '__dict__' of 'ValueArray' objects>, '__weakref__': <attribute '__weakref__' of 'ValueArray' objects>, '__doc__': None, 'n_values': <property object at 0x7fe46b8d0180>, 'values': <property object at 0x7fe46b8d0270>, 'n_prealloced': <property object at 0x7fe46b8d0360>, 'new': gi.FunctionInfo(new), 'append': gi.FunctionInfo(append), 'copy': gi.FunctionInfo(copy), 'get_nth': gi.FunctionInfo(get_nth), 'insert': gi.FunctionInfo(insert), 'prepend': gi.FunctionInfo(prepend), 'remove': gi.FunctionInfo(remove), 'sort': gi.FunctionInfo(sort)})"
    __gtype__ = None # (!) real value is '<GType GValueArray (94184341423200)>'
    __info__ = StructInfo(ValueArray)


