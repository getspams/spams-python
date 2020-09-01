__all__ = ['spams']

from pkg_resources import get_distribution
__version__ = get_distribution('spams').version

from .spams import *
