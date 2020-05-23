__all__ = ['myscipy_rand']

from pkg_resources import get_distribution
__version__ = get_distribution('spams-python').version

from .myscipy_rand import *

