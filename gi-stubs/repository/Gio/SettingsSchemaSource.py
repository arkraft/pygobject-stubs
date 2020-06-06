# encoding: utf-8
# module gi.repository.Gio
# from /usr/lib64/girepository-1.0/Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class SettingsSchemaSource(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_from_directory(directory:str, parent:Gio.SettingsSchemaSource=None, trusted:bool) -> Gio.SettingsSchemaSource
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Gio.SettingsSchemaSource or None """
        pass

    def list_schemas(self, recursive): # real signature unknown; restored from __doc__
        """ list_schemas(self, recursive:bool) -> non_relocatable:list, relocatable:list """
        pass

    def lookup(self, schema_id, recursive): # real signature unknown; restored from __doc__
        """ lookup(self, schema_id:str, recursive:bool) -> Gio.SettingsSchema or None """
        pass

    def new_from_directory(self, directory, parent=None, trusted): # real signature unknown; restored from __doc__
        """ new_from_directory(directory:str, parent:Gio.SettingsSchemaSource=None, trusted:bool) -> Gio.SettingsSchemaSource """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gio.SettingsSchemaSource """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SettingsSchemaSource), '__module__': 'gi.repository.Gio', '__gtype__': <GType GSettingsSchemaSource (94269257331344)>, '__dict__': <attribute '__dict__' of 'SettingsSchemaSource' objects>, '__weakref__': <attribute '__weakref__' of 'SettingsSchemaSource' objects>, '__doc__': None, 'new_from_directory': gi.FunctionInfo(new_from_directory), 'list_schemas': gi.FunctionInfo(list_schemas), 'lookup': gi.FunctionInfo(lookup), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), 'get_default': gi.FunctionInfo(get_default)})"
    __gtype__ = None # (!) real value is '<GType GSettingsSchemaSource (94269257331344)>'
    __info__ = StructInfo(SettingsSchemaSource)


