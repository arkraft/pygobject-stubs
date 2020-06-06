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


class EditableText(__gobject.GInterface):
    # no doc
    def copy_text(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ copy_text(self, start_pos:int, end_pos:int) """
        pass

    def cut_text(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ cut_text(self, start_pos:int, end_pos:int) """
        pass

    def delete_text(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ delete_text(self, start_pos:int, end_pos:int) """
        pass

    def insert_text(self, string, length, position): # real signature unknown; restored from __doc__
        """ insert_text(self, string:str, length:int, position:int) """
        pass

    def paste_text(self, position): # real signature unknown; restored from __doc__
        """ paste_text(self, position:int) """
        pass

    def set_run_attributes(self, attrib_set, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ set_run_attributes(self, attrib_set:list, start_offset:int, end_offset:int) -> bool """
        return False

    def set_text_contents(self, string): # real signature unknown; restored from __doc__
        """ set_text_contents(self, string:str) """
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(EditableText), '__module__': 'gi.repository.Atk', '__gtype__': <GType AtkEditableText (94258337624176)>, '__dict__': <attribute '__dict__' of 'EditableText' objects>, '__weakref__': <attribute '__weakref__' of 'EditableText' objects>, '__doc__': None, '__gsignals__': {}, 'copy_text': gi.FunctionInfo(copy_text), 'cut_text': gi.FunctionInfo(cut_text), 'delete_text': gi.FunctionInfo(delete_text), 'insert_text': gi.FunctionInfo(insert_text), 'paste_text': gi.FunctionInfo(paste_text), 'set_run_attributes': gi.FunctionInfo(set_run_attributes), 'set_text_contents': gi.FunctionInfo(set_text_contents)})"
    __gdoc__ = 'Interface AtkEditableText\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtkEditableText (94258337624176)>'
    __info__ = InterfaceInfo(EditableText)


