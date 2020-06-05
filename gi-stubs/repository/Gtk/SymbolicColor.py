# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class SymbolicColor(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_alpha(color:Gtk.SymbolicColor, factor:float) -> Gtk.SymbolicColor
        new_literal(color:Gdk.RGBA) -> Gtk.SymbolicColor
        new_mix(color1:Gtk.SymbolicColor, color2:Gtk.SymbolicColor, factor:float) -> Gtk.SymbolicColor
        new_name(name:str) -> Gtk.SymbolicColor
        new_shade(color:Gtk.SymbolicColor, factor:float) -> Gtk.SymbolicColor
        new_win32(theme_class:str, id:int) -> Gtk.SymbolicColor
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def new_alpha(self, color, factor): # real signature unknown; restored from __doc__
        """ new_alpha(color:Gtk.SymbolicColor, factor:float) -> Gtk.SymbolicColor """
        pass

    def new_literal(self, color): # real signature unknown; restored from __doc__
        """ new_literal(color:Gdk.RGBA) -> Gtk.SymbolicColor """
        pass

    def new_mix(self, color1, color2, factor): # real signature unknown; restored from __doc__
        """ new_mix(color1:Gtk.SymbolicColor, color2:Gtk.SymbolicColor, factor:float) -> Gtk.SymbolicColor """
        pass

    def new_name(self, name): # real signature unknown; restored from __doc__
        """ new_name(name:str) -> Gtk.SymbolicColor """
        pass

    def new_shade(self, color, factor): # real signature unknown; restored from __doc__
        """ new_shade(color:Gtk.SymbolicColor, factor:float) -> Gtk.SymbolicColor """
        pass

    def new_win32(self, theme_class, id): # real signature unknown; restored from __doc__
        """ new_win32(theme_class:str, id:int) -> Gtk.SymbolicColor """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gtk.SymbolicColor """
        pass

    def resolve(self, props=None): # real signature unknown; restored from __doc__
        """ resolve(self, props:Gtk.StyleProperties=None) -> bool, resolved_color:Gdk.RGBA """
        return False

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SymbolicColor), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkSymbolicColor (94846039358224)>, '__dict__': <attribute '__dict__' of 'SymbolicColor' objects>, '__weakref__': <attribute '__weakref__' of 'SymbolicColor' objects>, '__doc__': None, 'new_alpha': gi.FunctionInfo(new_alpha), 'new_literal': gi.FunctionInfo(new_literal), 'new_mix': gi.FunctionInfo(new_mix), 'new_name': gi.FunctionInfo(new_name), 'new_shade': gi.FunctionInfo(new_shade), 'new_win32': gi.FunctionInfo(new_win32), 'ref': gi.FunctionInfo(ref), 'resolve': gi.FunctionInfo(resolve), 'to_string': gi.FunctionInfo(to_string), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GtkSymbolicColor (94846039358224)>'
    __info__ = StructInfo(SymbolicColor)


