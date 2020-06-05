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


# Variables with simple values

ANALYSIS_FLAG_CENTERED_BASELINE = 1

ANALYSIS_FLAG_IS_ELLIPSIS = 2

ANALYSIS_FLAG_NEED_HYPHEN = 4

ATTR_INDEX_FROM_TEXT_BEGINNING = 0

ENGINE_TYPE_LANG = 'PangoEngineLang'
ENGINE_TYPE_SHAPE = 'PangoEngineShape'

GLYPH_EMPTY = 268435455

GLYPH_INVALID_INPUT = 4294967295

GLYPH_UNKNOWN_FLAG = 268435456

RENDER_TYPE_NONE = 'PangoRenderNone'

SCALE = 1024

UNKNOWN_GLYPH_HEIGHT = 14
UNKNOWN_GLYPH_WIDTH = 10

VERSION_MIN_REQUIRED = 2

_namespace = 'Pango'

_version = '1.0'

__weakref__ = None

# functions

def attr_allow_breaks_new(allow_breaks): # real signature unknown; restored from __doc__
    """ attr_allow_breaks_new(allow_breaks:bool) -> Pango.Attribute """
    pass

def attr_background_alpha_new(alpha): # real signature unknown; restored from __doc__
    """ attr_background_alpha_new(alpha:int) -> Pango.Attribute """
    pass

def attr_background_new(red, green, blue): # real signature unknown; restored from __doc__
    """ attr_background_new(red:int, green:int, blue:int) -> Pango.Attribute """
    pass

def attr_fallback_new(enable_fallback): # real signature unknown; restored from __doc__
    """ attr_fallback_new(enable_fallback:bool) -> Pango.Attribute """
    pass

def attr_family_new(family): # real signature unknown; restored from __doc__
    """ attr_family_new(family:str) -> Pango.Attribute """
    pass

def attr_font_desc_new(desc): # real signature unknown; restored from __doc__
    """ attr_font_desc_new(desc:Pango.FontDescription) -> Pango.Attribute """
    pass

def attr_font_features_new(features): # real signature unknown; restored from __doc__
    """ attr_font_features_new(features:str) -> Pango.Attribute """
    pass

def attr_foreground_alpha_new(alpha): # real signature unknown; restored from __doc__
    """ attr_foreground_alpha_new(alpha:int) -> Pango.Attribute """
    pass

def attr_foreground_new(red, green, blue): # real signature unknown; restored from __doc__
    """ attr_foreground_new(red:int, green:int, blue:int) -> Pango.Attribute """
    pass

def attr_gravity_hint_new(hint): # real signature unknown; restored from __doc__
    """ attr_gravity_hint_new(hint:Pango.GravityHint) -> Pango.Attribute """
    pass

def attr_gravity_new(gravity): # real signature unknown; restored from __doc__
    """ attr_gravity_new(gravity:Pango.Gravity) -> Pango.Attribute """
    pass

def attr_insert_hyphens_new(insert_hyphens): # real signature unknown; restored from __doc__
    """ attr_insert_hyphens_new(insert_hyphens:bool) -> Pango.Attribute """
    pass

def attr_language_new(language): # real signature unknown; restored from __doc__
    """ attr_language_new(language:Pango.Language) -> Pango.Attribute """
    pass

def attr_letter_spacing_new(letter_spacing): # real signature unknown; restored from __doc__
    """ attr_letter_spacing_new(letter_spacing:int) -> Pango.Attribute """
    pass

def attr_rise_new(rise): # real signature unknown; restored from __doc__
    """ attr_rise_new(rise:int) -> Pango.Attribute """
    pass

def attr_scale_new(scale_factor): # real signature unknown; restored from __doc__
    """ attr_scale_new(scale_factor:float) -> Pango.Attribute """
    pass

def attr_shape_new(ink_rect, logical_rect): # real signature unknown; restored from __doc__
    """ attr_shape_new(ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle) -> Pango.Attribute """
    pass

def attr_shape_new_with_data(ink_rect, logical_rect, data=None, copy_func=None): # real signature unknown; restored from __doc__
    """ attr_shape_new_with_data(ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle, data=None, copy_func:Pango.AttrDataCopyFunc=None) -> Pango.Attribute """
    pass

def attr_show_new(flags): # real signature unknown; restored from __doc__
    """ attr_show_new(flags:Pango.ShowFlags) -> Pango.Attribute """
    pass

def attr_size_new(size): # real signature unknown; restored from __doc__
    """ attr_size_new(size:int) -> Pango.Attribute """
    pass

def attr_size_new_absolute(size): # real signature unknown; restored from __doc__
    """ attr_size_new_absolute(size:int) -> Pango.Attribute """
    pass

def attr_stretch_new(stretch): # real signature unknown; restored from __doc__
    """ attr_stretch_new(stretch:Pango.Stretch) -> Pango.Attribute """
    pass

def attr_strikethrough_color_new(red, green, blue): # real signature unknown; restored from __doc__
    """ attr_strikethrough_color_new(red:int, green:int, blue:int) -> Pango.Attribute """
    pass

def attr_strikethrough_new(strikethrough): # real signature unknown; restored from __doc__
    """ attr_strikethrough_new(strikethrough:bool) -> Pango.Attribute """
    pass

def attr_style_new(style): # real signature unknown; restored from __doc__
    """ attr_style_new(style:Pango.Style) -> Pango.Attribute """
    pass

def attr_type_get_name(type): # real signature unknown; restored from __doc__
    """ attr_type_get_name(type:Pango.AttrType) -> str or None """
    return ""

def attr_type_register(name): # real signature unknown; restored from __doc__
    """ attr_type_register(name:str) -> Pango.AttrType """
    pass

def attr_underline_color_new(red, green, blue): # real signature unknown; restored from __doc__
    """ attr_underline_color_new(red:int, green:int, blue:int) -> Pango.Attribute """
    pass

def attr_underline_new(underline): # real signature unknown; restored from __doc__
    """ attr_underline_new(underline:Pango.Underline) -> Pango.Attribute """
    pass

def attr_variant_new(variant): # real signature unknown; restored from __doc__
    """ attr_variant_new(variant:Pango.Variant) -> Pango.Attribute """
    pass

def attr_weight_new(weight): # real signature unknown; restored from __doc__
    """ attr_weight_new(weight:Pango.Weight) -> Pango.Attribute """
    pass

def bidi_type_for_unichar(ch): # real signature unknown; restored from __doc__
    """ bidi_type_for_unichar(ch:str) -> Pango.BidiType """
    pass

def break_(text, length, analysis, attrs): # real signature unknown; restored from __doc__
    """ break_(text:str, length:int, analysis:Pango.Analysis, attrs:list) """
    pass

def default_break(text, length, analysis=None, attrs, attrs_len): # real signature unknown; restored from __doc__
    """ default_break(text:str, length:int, analysis:Pango.Analysis=None, attrs:Pango.LogAttr, attrs_len:int) """
    pass

def extents_to_pixels(inclusive=None, nearest=None): # real signature unknown; restored from __doc__
    """ extents_to_pixels(inclusive:Pango.Rectangle=None, nearest:Pango.Rectangle=None) """
    pass

def find_base_dir(text, length): # real signature unknown; restored from __doc__
    """ find_base_dir(text:str, length:int) -> Pango.Direction """
    pass

def find_paragraph_boundary(text, length): # real signature unknown; restored from __doc__
    """ find_paragraph_boundary(text:str, length:int) -> paragraph_delimiter_index:int, next_paragraph_start:int """
    pass

def font_description_from_string(p_str): # real signature unknown; restored from __doc__
    """ font_description_from_string(str:str) -> Pango.FontDescription """
    pass

def get_log_attrs(text, length, level, language, log_attrs): # real signature unknown; restored from __doc__
    """ get_log_attrs(text:str, length:int, level:int, language:Pango.Language, log_attrs:list) """
    pass

def get_mirror_char(ch, mirrored_ch): # real signature unknown; restored from __doc__
    """ get_mirror_char(ch:str, mirrored_ch:str) -> bool """
    return False

def gravity_get_for_matrix(matrix=None): # real signature unknown; restored from __doc__
    """ gravity_get_for_matrix(matrix:Pango.Matrix=None) -> Pango.Gravity """
    pass

def gravity_get_for_script(script, base_gravity, hint): # real signature unknown; restored from __doc__
    """ gravity_get_for_script(script:Pango.Script, base_gravity:Pango.Gravity, hint:Pango.GravityHint) -> Pango.Gravity """
    pass

def gravity_get_for_script_and_width(script, wide, base_gravity, hint): # real signature unknown; restored from __doc__
    """ gravity_get_for_script_and_width(script:Pango.Script, wide:bool, base_gravity:Pango.Gravity, hint:Pango.GravityHint) -> Pango.Gravity """
    pass

def gravity_to_rotation(gravity): # real signature unknown; restored from __doc__
    """ gravity_to_rotation(gravity:Pango.Gravity) -> float """
    return 0.0

def is_zero_width(ch): # real signature unknown; restored from __doc__
    """ is_zero_width(ch:str) -> bool """
    return False

def itemize(context, text, start_index, length, attrs, cached_iter=None): # real signature unknown; restored from __doc__
    """ itemize(context:Pango.Context, text:str, start_index:int, length:int, attrs:Pango.AttrList, cached_iter:Pango.AttrIterator=None) -> list """
    return []

def itemize_with_base_dir(context, base_dir, text, start_index, length, attrs, cached_iter=None): # real signature unknown; restored from __doc__
    """ itemize_with_base_dir(context:Pango.Context, base_dir:Pango.Direction, text:str, start_index:int, length:int, attrs:Pango.AttrList, cached_iter:Pango.AttrIterator=None) -> list """
    return []

def language_from_string(language=None): # real signature unknown; restored from __doc__
    """ language_from_string(language:str=None) -> Pango.Language or None """
    pass

def language_get_default(): # real signature unknown; restored from __doc__
    """ language_get_default() -> Pango.Language """
    pass

def log2vis_get_embedding_levels(text, length, pbase_dir): # real signature unknown; restored from __doc__
    """ log2vis_get_embedding_levels(text:str, length:int, pbase_dir:Pango.Direction) -> int """
    return 0

def markup_parser_finish(context): # real signature unknown; restored from __doc__
    """ markup_parser_finish(context:GLib.MarkupParseContext) -> bool, attr_list:Pango.AttrList, text:str, accel_char:str """
    return False

def markup_parser_new(accel_marker): # real signature unknown; restored from __doc__
    """ markup_parser_new(accel_marker:str) -> GLib.MarkupParseContext """
    pass

def parse_enum(type, p_str=None, warn): # real signature unknown; restored from __doc__
    """ parse_enum(type:GType, str:str=None, warn:bool) -> bool, value:int, possible_values:str """
    return False

def parse_markup(markup_text, length, accel_marker): # real signature unknown; restored from __doc__
    """ parse_markup(markup_text:str, length:int, accel_marker:str) -> bool, attr_list:Pango.AttrList, text:str, accel_char:str """
    return False

def parse_stretch(p_str, warn): # real signature unknown; restored from __doc__
    """ parse_stretch(str:str, warn:bool) -> bool, stretch:Pango.Stretch """
    return False

def parse_style(p_str, warn): # real signature unknown; restored from __doc__
    """ parse_style(str:str, warn:bool) -> bool, style:Pango.Style """
    return False

def parse_variant(p_str, warn): # real signature unknown; restored from __doc__
    """ parse_variant(str:str, warn:bool) -> bool, variant:Pango.Variant """
    return False

def parse_weight(p_str, warn): # real signature unknown; restored from __doc__
    """ parse_weight(str:str, warn:bool) -> bool, weight:Pango.Weight """
    return False

def quantize_line_geometry(thickness, position): # real signature unknown; restored from __doc__
    """ quantize_line_geometry(thickness:int, position:int) -> thickness:int, position:int """
    pass

def read_line(stream=None, p_str): # real signature unknown; restored from __doc__
    """ read_line(stream=None, str:GLib.String) -> int """
    return 0

def reorder_items(logical_items): # real signature unknown; restored from __doc__
    """ reorder_items(logical_items:list) -> list """
    return []

def scan_int(pos): # real signature unknown; restored from __doc__
    """ scan_int(pos:str) -> bool, pos:str, out:int """
    return False

def scan_string(pos, out): # real signature unknown; restored from __doc__
    """ scan_string(pos:str, out:GLib.String) -> bool, pos:str """
    return False

def scan_word(pos, out): # real signature unknown; restored from __doc__
    """ scan_word(pos:str, out:GLib.String) -> bool, pos:str """
    return False

def script_for_unichar(ch): # real signature unknown; restored from __doc__
    """ script_for_unichar(ch:str) -> Pango.Script """
    pass

def script_get_sample_language(script): # real signature unknown; restored from __doc__
    """ script_get_sample_language(script:Pango.Script) -> Pango.Language or None """
    pass

def shape(text, length, analysis, glyphs): # real signature unknown; restored from __doc__
    """ shape(text:str, length:int, analysis:Pango.Analysis, glyphs:Pango.GlyphString) """
    pass

def shape_full(item_text, item_length, paragraph_text=None, paragraph_length, analysis, glyphs): # real signature unknown; restored from __doc__
    """ shape_full(item_text:str, item_length:int, paragraph_text:str=None, paragraph_length:int, analysis:Pango.Analysis, glyphs:Pango.GlyphString) """
    pass

def shape_with_flags(item_text, item_length, paragraph_text=None, paragraph_length, analysis, glyphs, flags): # real signature unknown; restored from __doc__
    """ shape_with_flags(item_text:str, item_length:int, paragraph_text:str=None, paragraph_length:int, analysis:Pango.Analysis, glyphs:Pango.GlyphString, flags:Pango.ShapeFlags) """
    pass

def skip_space(pos): # real signature unknown; restored from __doc__
    """ skip_space(pos:str) -> bool, pos:str """
    return False

def split_file_list(p_str): # real signature unknown; restored from __doc__
    """ split_file_list(str:str) -> list """
    return []

def tailor_break(text, length, analysis, offset, log_attrs): # real signature unknown; restored from __doc__
    """ tailor_break(text:str, length:int, analysis:Pango.Analysis, offset:int, log_attrs:list) """
    pass

def trim_string(p_str): # real signature unknown; restored from __doc__
    """ trim_string(str:str) -> str """
    return ""

def unichar_direction(ch): # real signature unknown; restored from __doc__
    """ unichar_direction(ch:str) -> Pango.Direction """
    pass

def units_from_double(d): # real signature unknown; restored from __doc__
    """ units_from_double(d:float) -> int """
    return 0

def units_to_double(i): # real signature unknown; restored from __doc__
    """ units_to_double(i:int) -> float """
    return 0.0

def version(): # real signature unknown; restored from __doc__
    """ version() -> int """
    return 0

def version_check(required_major, required_minor, required_micro): # real signature unknown; restored from __doc__
    """ version_check(required_major:int, required_minor:int, required_micro:int) -> str or None """
    return ""

def version_string(): # real signature unknown; restored from __doc__
    """ version_string() -> str """
    return ""

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .Alignment import Alignment
from .Analysis import Analysis
from .AttrClass import AttrClass
from .AttrColor import AttrColor
from .AttrFloat import AttrFloat
from .AttrFontDesc import AttrFontDesc
from .AttrFontFeatures import AttrFontFeatures
from .Attribute import Attribute
from .AttrInt import AttrInt
from .AttrIterator import AttrIterator
from .AttrLanguage import AttrLanguage
from .AttrList import AttrList
from .AttrShape import AttrShape
from .AttrSize import AttrSize
from .AttrString import AttrString
from .AttrType import AttrType
from .BidiType import BidiType
from .Color import Color
from .Context import Context
from .ContextClass import ContextClass
from .Coverage import Coverage
from .CoverageLevel import CoverageLevel
from .Direction import Direction
from .EllipsizeMode import EllipsizeMode
from .Engine import Engine
from .EngineClass import EngineClass
from .EngineInfo import EngineInfo
from .EngineLang import EngineLang
from .EngineLangClass import EngineLangClass
from .EngineScriptInfo import EngineScriptInfo
from .EngineShape import EngineShape
from .EngineShapeClass import EngineShapeClass
from .Font import Font
from .FontClass import FontClass
from .FontDescription import FontDescription
from .FontFace import FontFace
from .FontFaceClass import FontFaceClass
from .FontFamily import FontFamily
from .FontFamilyClass import FontFamilyClass
from .FontMap import FontMap
from .FontMapClass import FontMapClass
from .FontMask import FontMask
from .FontMetrics import FontMetrics
from .Fontset import Fontset
from .FontsetClass import FontsetClass
from .FontsetSimple import FontsetSimple
from .FontsetSimpleClass import FontsetSimpleClass
from .GlyphGeometry import GlyphGeometry
from .GlyphInfo import GlyphInfo
from .GlyphItem import GlyphItem
from .GlyphItemIter import GlyphItemIter
from .GlyphString import GlyphString
from .GlyphVisAttr import GlyphVisAttr
from .Gravity import Gravity
from .GravityHint import GravityHint
from .IncludedModule import IncludedModule
from .Item import Item
from .Language import Language
from .Layout import Layout
from .LayoutClass import LayoutClass
from .LayoutIter import LayoutIter
from .LayoutLine import LayoutLine
from .LogAttr import LogAttr
from .Map import Map
from .MapEntry import MapEntry
from .Matrix import Matrix
from .Rectangle import Rectangle
from .Renderer import Renderer
from .RendererClass import RendererClass
from .RendererPrivate import RendererPrivate
from .RenderPart import RenderPart
from .Script import Script
from .ScriptIter import ScriptIter
from .ShapeFlags import ShapeFlags
from .ShowFlags import ShowFlags
from .Stretch import Stretch
from .Style import Style
from .TabAlign import TabAlign
from .TabArray import TabArray
from .Underline import Underline
from .Variant import Variant
from .Weight import Weight
from .WrapMode import WrapMode
from .__class__ import __class__
# variables with complex values

_introspection_module = None # (!) real value is "<IntrospectionModule 'Pango' from '/usr/lib64/girepository-1.0/Pango-1.0.typelib'>"

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f24756b59d0>'

__path__ = [
    '/usr/lib64/girepository-1.0/Pango-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Pango', loader=<gi.importer.DynamicImporter object at 0x7f24756b59d0>)"

