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


class Regex(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(pattern:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> GLib.Regex or None
    """
    def check_replacement(self, replacement): # real signature unknown; restored from __doc__
        """ check_replacement(replacement:str) -> bool, has_references:bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def escape_nul(self, string, length): # real signature unknown; restored from __doc__
        """ escape_nul(string:str, length:int) -> str """
        return ""

    def escape_string(self, string): # real signature unknown; restored from __doc__
        """ escape_string(string:list) -> str """
        return ""

    def get_capture_count(self): # real signature unknown; restored from __doc__
        """ get_capture_count(self) -> int """
        return 0

    def get_compile_flags(self): # real signature unknown; restored from __doc__
        """ get_compile_flags(self) -> GLib.RegexCompileFlags """
        pass

    def get_has_cr_or_lf(self): # real signature unknown; restored from __doc__
        """ get_has_cr_or_lf(self) -> bool """
        return False

    def get_match_flags(self): # real signature unknown; restored from __doc__
        """ get_match_flags(self) -> GLib.RegexMatchFlags """
        pass

    def get_max_backref(self): # real signature unknown; restored from __doc__
        """ get_max_backref(self) -> int """
        return 0

    def get_max_lookbehind(self): # real signature unknown; restored from __doc__
        """ get_max_lookbehind(self) -> int """
        return 0

    def get_pattern(self): # real signature unknown; restored from __doc__
        """ get_pattern(self) -> str """
        return ""

    def get_string_number(self, name): # real signature unknown; restored from __doc__
        """ get_string_number(self, name:str) -> int """
        return 0

    def match(self, string, match_options): # real signature unknown; restored from __doc__
        """ match(self, string:str, match_options:GLib.RegexMatchFlags) -> bool, match_info:GLib.MatchInfo """
        return False

    def match_all(self, string, match_options): # real signature unknown; restored from __doc__
        """ match_all(self, string:str, match_options:GLib.RegexMatchFlags) -> bool, match_info:GLib.MatchInfo """
        return False

    def match_all_full(self, string, start_position, match_options): # real signature unknown; restored from __doc__
        """ match_all_full(self, string:list, start_position:int, match_options:GLib.RegexMatchFlags) -> bool, match_info:GLib.MatchInfo """
        return False

    def match_full(self, string, start_position, match_options): # real signature unknown; restored from __doc__
        """ match_full(self, string:list, start_position:int, match_options:GLib.RegexMatchFlags) -> bool, match_info:GLib.MatchInfo """
        return False

    def match_simple(self, pattern, string, compile_options, match_options): # real signature unknown; restored from __doc__
        """ match_simple(pattern:str, string:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> bool """
        return False

    def new(self, pattern, compile_options, match_options): # real signature unknown; restored from __doc__
        """ new(pattern:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> GLib.Regex or None """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.Regex """
        pass

    def replace(self, string, start_position, replacement, match_options): # real signature unknown; restored from __doc__
        """ replace(self, string:list, start_position:int, replacement:str, match_options:GLib.RegexMatchFlags) -> str """
        return ""

    def replace_literal(self, string, start_position, replacement, match_options): # real signature unknown; restored from __doc__
        """ replace_literal(self, string:list, start_position:int, replacement:str, match_options:GLib.RegexMatchFlags) -> str """
        return ""

    def split(self, string, match_options): # real signature unknown; restored from __doc__
        """ split(self, string:str, match_options:GLib.RegexMatchFlags) -> list """
        return []

    def split_full(self, string, start_position, match_options, max_tokens): # real signature unknown; restored from __doc__
        """ split_full(self, string:list, start_position:int, match_options:GLib.RegexMatchFlags, max_tokens:int) -> list """
        return []

    def split_simple(self, pattern, string, compile_options, match_options): # real signature unknown; restored from __doc__
        """ split_simple(pattern:str, string:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> list """
        return []

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
        """ new(pattern:str, compile_options:GLib.RegexCompileFlags, match_options:GLib.RegexMatchFlags) -> GLib.Regex or None """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Regex), '__module__': 'gi.repository.GLib', '__gtype__': <GType GRegex (94243599043536)>, '__dict__': <attribute '__dict__' of 'Regex' objects>, '__weakref__': <attribute '__weakref__' of 'Regex' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'get_capture_count': gi.FunctionInfo(get_capture_count), 'get_compile_flags': gi.FunctionInfo(get_compile_flags), 'get_has_cr_or_lf': gi.FunctionInfo(get_has_cr_or_lf), 'get_match_flags': gi.FunctionInfo(get_match_flags), 'get_max_backref': gi.FunctionInfo(get_max_backref), 'get_max_lookbehind': gi.FunctionInfo(get_max_lookbehind), 'get_pattern': gi.FunctionInfo(get_pattern), 'get_string_number': gi.FunctionInfo(get_string_number), 'match': gi.FunctionInfo(match), 'match_all': gi.FunctionInfo(match_all), 'match_all_full': gi.FunctionInfo(match_all_full), 'match_full': gi.FunctionInfo(match_full), 'ref': gi.FunctionInfo(ref), 'replace': gi.FunctionInfo(replace), 'replace_literal': gi.FunctionInfo(replace_literal), 'split': gi.FunctionInfo(split), 'split_full': gi.FunctionInfo(split_full), 'unref': gi.FunctionInfo(unref), 'check_replacement': gi.FunctionInfo(check_replacement), 'error_quark': gi.FunctionInfo(error_quark), 'escape_nul': gi.FunctionInfo(escape_nul), 'escape_string': gi.FunctionInfo(escape_string), 'match_simple': gi.FunctionInfo(match_simple), 'split_simple': gi.FunctionInfo(split_simple), '__new__': <staticmethod object at 0x7f1d2b8f19a0>, '__init__': <function nothing at 0x7f1d2baee430>})"
    __gtype__ = None # (!) real value is '<GType GRegex (94243599043536)>'
    __info__ = StructInfo(Regex)


