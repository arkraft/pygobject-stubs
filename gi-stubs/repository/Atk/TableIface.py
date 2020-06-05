# encoding: utf-8
# module gi.repository.Atk
# from /usr/lib64/girepository-1.0/Atk-1.0.typelib
# by generator 1.147
"""
An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
"""

# imports
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


class TableIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TableIface()
    """
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

    add_column_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add_row_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    column_deleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    column_inserted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    column_reordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_caption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_column_at_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_column_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_column_extent_at = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_column_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_index_at = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_row_at_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_row_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_row_extent_at = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_row_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_selected_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_selected_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_column_selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_row_selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_at = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_column_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_row_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_deleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_inserted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_reordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_caption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_column_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_column_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_row_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_row_header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TableIface), '__module__': 'gi.repository.Atk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TableIface' objects>, '__weakref__': <attribute '__weakref__' of 'TableIface' objects>, '__doc__': None, 'parent': <property object at 0x7f0cd81bcea0>, 'ref_at': <property object at 0x7f0cd81bcf90>, 'get_index_at': <property object at 0x7f0cd81bd0e0>, 'get_column_at_index': <property object at 0x7f0cd81bd220>, 'get_row_at_index': <property object at 0x7f0cd81bd310>, 'get_n_columns': <property object at 0x7f0cd81bd3b0>, 'get_n_rows': <property object at 0x7f0cd81bd4a0>, 'get_column_extent_at': <property object at 0x7f0cd81bd5e0>, 'get_row_extent_at': <property object at 0x7f0cd81bd6d0>, 'get_caption': <property object at 0x7f0cd81bd770>, 'get_column_description': <property object at 0x7f0cd81bd8b0>, 'get_column_header': <property object at 0x7f0cd81bd9a0>, 'get_row_description': <property object at 0x7f0cd81bda90>, 'get_row_header': <property object at 0x7f0cd81bdb30>, 'get_summary': <property object at 0x7f0cd81bdc20>, 'set_caption': <property object at 0x7f0cd81bdd10>, 'set_column_description': <property object at 0x7f0cd81bde50>, 'set_column_header': <property object at 0x7f0cd81bdf40>, 'set_row_description': <property object at 0x7f0cd81be090>, 'set_row_header': <property object at 0x7f0cd81be130>, 'set_summary': <property object at 0x7f0cd81be220>, 'get_selected_columns': <property object at 0x7f0cd81be360>, 'get_selected_rows': <property object at 0x7f0cd81be450>, 'is_column_selected': <property object at 0x7f0cd81be540>, 'is_row_selected': <property object at 0x7f0cd81be5e0>, 'is_selected': <property object at 0x7f0cd81be6d0>, 'add_row_selection': <property object at 0x7f0cd81be810>, 'remove_row_selection': <property object at 0x7f0cd81be900>, 'add_column_selection': <property object at 0x7f0cd81be9f0>, 'remove_column_selection': <property object at 0x7f0cd81beae0>, 'row_inserted': <property object at 0x7f0cd81beb80>, 'column_inserted': <property object at 0x7f0cd81bec70>, 'row_deleted': <property object at 0x7f0cd81bed60>, 'column_deleted': <property object at 0x7f0cd81bee50>, 'row_reordered': <property object at 0x7f0cd81bef40>, 'column_reordered': <property object at 0x7f0cd81bf0e0>, 'model_changed': <property object at 0x7f0cd81bf1d0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TableIface)


