# encoding: utf-8
# module gi.repository.Pango
# from /usr/lib64/girepository-1.0/Pango-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


class AttrShape(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        AttrShape()
    """
    def new(self, ink_rect, logical_rect): # real signature unknown; restored from __doc__
        """ new(ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle) -> Pango.Attribute """
        pass

    def new_with_data(self, ink_rect, logical_rect, data=None, copy_func=None): # real signature unknown; restored from __doc__
        """ new_with_data(ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle, data=None, copy_func:Pango.AttrDataCopyFunc=None) -> Pango.Attribute """
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

    attr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destroy_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ink_rect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    logical_rect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AttrShape), '__module__': 'gi.repository.Pango', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AttrShape' objects>, '__weakref__': <attribute '__weakref__' of 'AttrShape' objects>, '__doc__': None, 'attr': <property object at 0x7f8517884c20>, 'ink_rect': <property object at 0x7f8517884d10>, 'logical_rect': <property object at 0x7f8517884e00>, 'data': <property object at 0x7f8517884ef0>, 'copy_func': <property object at 0x7f8517885040>, 'destroy_func': <property object at 0x7f8517885130>, 'new': gi.FunctionInfo(new), 'new_with_data': gi.FunctionInfo(new_with_data)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AttrShape)


