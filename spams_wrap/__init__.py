__all__ = ['spams_wrap', 'decomp','dictLearn','linalg','prox']

from pkg_resources import get_distribution
__version__ = get_distribution('spams').version

from .spams_wrap import *
