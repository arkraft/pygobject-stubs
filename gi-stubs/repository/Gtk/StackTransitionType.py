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


class StackTransitionType(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CROSSFADE = 1
    NONE = 0
    OVER_DOWN = 9
    OVER_DOWN_UP = 17
    OVER_LEFT = 10
    OVER_LEFT_RIGHT = 18
    OVER_RIGHT = 11
    OVER_RIGHT_LEFT = 19
    OVER_UP = 8
    OVER_UP_DOWN = 16
    SLIDE_DOWN = 5
    SLIDE_LEFT = 3
    SLIDE_LEFT_RIGHT = 6
    SLIDE_RIGHT = 2
    SLIDE_UP = 4
    SLIDE_UP_DOWN = 7
    UNDER_DOWN = 13
    UNDER_LEFT = 14
    UNDER_RIGHT = 15
    UNDER_UP = 12
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gtk', '__dict__': <attribute '__dict__' of 'StackTransitionType' objects>, '__doc__': None, '__gtype__': <GType GtkStackTransitionType (94846039278288)>, '__enum_values__': {0: <enum GTK_STACK_TRANSITION_TYPE_NONE of type Gtk.StackTransitionType>, 1: <enum GTK_STACK_TRANSITION_TYPE_CROSSFADE of type Gtk.StackTransitionType>, 2: <enum GTK_STACK_TRANSITION_TYPE_SLIDE_RIGHT of type Gtk.StackTransitionType>, 3: <enum GTK_STACK_TRANSITION_TYPE_SLIDE_LEFT of type Gtk.StackTransitionType>, 4: <enum GTK_STACK_TRANSITION_TYPE_SLIDE_UP of type Gtk.StackTransitionType>, 5: <enum GTK_STACK_TRANSITION_TYPE_SLIDE_DOWN of type Gtk.StackTransitionType>, 6: <enum GTK_STACK_TRANSITION_TYPE_SLIDE_LEFT_RIGHT of type Gtk.StackTransitionType>, 7: <enum GTK_STACK_TRANSITION_TYPE_SLIDE_UP_DOWN of type Gtk.StackTransitionType>, 8: <enum GTK_STACK_TRANSITION_TYPE_OVER_UP of type Gtk.StackTransitionType>, 9: <enum GTK_STACK_TRANSITION_TYPE_OVER_DOWN of type Gtk.StackTransitionType>, 10: <enum GTK_STACK_TRANSITION_TYPE_OVER_LEFT of type Gtk.StackTransitionType>, 11: <enum GTK_STACK_TRANSITION_TYPE_OVER_RIGHT of type Gtk.StackTransitionType>, 12: <enum GTK_STACK_TRANSITION_TYPE_UNDER_UP of type Gtk.StackTransitionType>, 13: <enum GTK_STACK_TRANSITION_TYPE_UNDER_DOWN of type Gtk.StackTransitionType>, 14: <enum GTK_STACK_TRANSITION_TYPE_UNDER_LEFT of type Gtk.StackTransitionType>, 15: <enum GTK_STACK_TRANSITION_TYPE_UNDER_RIGHT of type Gtk.StackTransitionType>, 16: <enum GTK_STACK_TRANSITION_TYPE_OVER_UP_DOWN of type Gtk.StackTransitionType>, 17: <enum GTK_STACK_TRANSITION_TYPE_OVER_DOWN_UP of type Gtk.StackTransitionType>, 18: <enum GTK_STACK_TRANSITION_TYPE_OVER_LEFT_RIGHT of type Gtk.StackTransitionType>, 19: <enum GTK_STACK_TRANSITION_TYPE_OVER_RIGHT_LEFT of type Gtk.StackTransitionType>}, '__info__': gi.EnumInfo(StackTransitionType), 'NONE': <enum GTK_STACK_TRANSITION_TYPE_NONE of type Gtk.StackTransitionType>, 'CROSSFADE': <enum GTK_STACK_TRANSITION_TYPE_CROSSFADE of type Gtk.StackTransitionType>, 'SLIDE_RIGHT': <enum GTK_STACK_TRANSITION_TYPE_SLIDE_RIGHT of type Gtk.StackTransitionType>, 'SLIDE_LEFT': <enum GTK_STACK_TRANSITION_TYPE_SLIDE_LEFT of type Gtk.StackTransitionType>, 'SLIDE_UP': <enum GTK_STACK_TRANSITION_TYPE_SLIDE_UP of type Gtk.StackTransitionType>, 'SLIDE_DOWN': <enum GTK_STACK_TRANSITION_TYPE_SLIDE_DOWN of type Gtk.StackTransitionType>, 'SLIDE_LEFT_RIGHT': <enum GTK_STACK_TRANSITION_TYPE_SLIDE_LEFT_RIGHT of type Gtk.StackTransitionType>, 'SLIDE_UP_DOWN': <enum GTK_STACK_TRANSITION_TYPE_SLIDE_UP_DOWN of type Gtk.StackTransitionType>, 'OVER_UP': <enum GTK_STACK_TRANSITION_TYPE_OVER_UP of type Gtk.StackTransitionType>, 'OVER_DOWN': <enum GTK_STACK_TRANSITION_TYPE_OVER_DOWN of type Gtk.StackTransitionType>, 'OVER_LEFT': <enum GTK_STACK_TRANSITION_TYPE_OVER_LEFT of type Gtk.StackTransitionType>, 'OVER_RIGHT': <enum GTK_STACK_TRANSITION_TYPE_OVER_RIGHT of type Gtk.StackTransitionType>, 'UNDER_UP': <enum GTK_STACK_TRANSITION_TYPE_UNDER_UP of type Gtk.StackTransitionType>, 'UNDER_DOWN': <enum GTK_STACK_TRANSITION_TYPE_UNDER_DOWN of type Gtk.StackTransitionType>, 'UNDER_LEFT': <enum GTK_STACK_TRANSITION_TYPE_UNDER_LEFT of type Gtk.StackTransitionType>, 'UNDER_RIGHT': <enum GTK_STACK_TRANSITION_TYPE_UNDER_RIGHT of type Gtk.StackTransitionType>, 'OVER_UP_DOWN': <enum GTK_STACK_TRANSITION_TYPE_OVER_UP_DOWN of type Gtk.StackTransitionType>, 'OVER_DOWN_UP': <enum GTK_STACK_TRANSITION_TYPE_OVER_DOWN_UP of type Gtk.StackTransitionType>, 'OVER_LEFT_RIGHT': <enum GTK_STACK_TRANSITION_TYPE_OVER_LEFT_RIGHT of type Gtk.StackTransitionType>, 'OVER_RIGHT_LEFT': <enum GTK_STACK_TRANSITION_TYPE_OVER_RIGHT_LEFT of type Gtk.StackTransitionType>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
    }
    __gtype__ = None # (!) real value is '<GType GtkStackTransitionType (94846039278288)>'
    __info__ = gi.EnumInfo(StackTransitionType)


