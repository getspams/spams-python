import os
from distutils.sysconfig import get_python_inc
from distutils.util import get_platform
import platform
import sys

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext


def get_config():
    # Import numpy here, only when headers are needed
    import numpy as np
    from numpy.distutils.system_info import blas_info

    incs = ['spams_wrap']
    for x in ['linalg', 'prox', 'decomp', 'dictLearn']:
        incs.append(os.path.join('spams_wrap', x))
    incs.append(np.get_include())
    incs.append(get_python_inc())
    incs.extend(blas_info().get_include_dirs())

    cc_flags = ['-fPIC', '-Wunused-variable', '-Wno-uninitialized']
    if sys.maxsize > 2**32:
        cc_flags.append('-m64')
    else:
        cc_flags.append('-m32')

    for _ in np.__config__.blas_opt_info.get('extra_compile_args', []):
        if _ not in cc_flags:
            cc_flags.append(_)
    for _ in np.__config__.lapack_opt_info.get('extra_compile_args', []):
        if _ not in cc_flags:
            cc_flags.append(_)

    link_flags = []
    for _ in np.__config__.blas_opt_info.get('extra_link_args', []):
        if _ not in link_flags:
            link_flags.append(_)
    for _ in np.__config__.lapack_opt_info.get('extra_link_args', []):
        if _ not in link_flags:
            link_flags.append(_)

    libs = ['stdc++']
    is_mkl = False
    for lib in np.__config__.blas_opt_info.get('libraries', []):
        if 'mkl' in lib:
            is_mkl = True
            break

    libdirs = np.distutils.system_info.blas_info().get_lib_dirs()
    if is_mkl:
        for _ in np.__config__.blas_opt_info.get('include_dirs', []):
            if _ not in incs:
                incs.append(_)
        for _ in np.__config__.blas_opt_info.get('library_dirs', []):
            if _ not in libdirs:
                libdirs.append(_)
        libs.extend(['mkl_rt'])
    else:
        libs.extend(['blas', 'lapack'])

    if platform.system() != 'Darwin':
        cc_flags.append('-fopenmp')
        link_flags.append('-fopenmp')

    return incs, libs, libdirs, cc_flags, link_flags


class CustomBuildExtCommand(build_ext):
    """ build_ext command to use when numpy headers are needed. """

    def run(self):
        # Now that the requirements are installed, get everything from numpy
        incs, libs, libdirs, cc_flags, link_flags = get_config()

        # Add everything requires for build
        self.extensions[0].include_dirs.extend(incs)
        self.extensions[0].libraries.extend(libs)
        self.extensions[0].library_dirs.extend(libdirs)

        self.extensions[0].extra_compile_args.extend(cc_flags)
        self.extensions[0].extra_link_args.extend(link_flags)

        # Call original build_ext command
        build_ext.run(self)


def get_extension():
    # Generic initialization of the extension
    spams_wrap = Extension('_spams_wrap',
                           sources=['spams_wrap/spams_wrap.cpp'],
                           extra_compile_args=['-DNDEBUG',
                                               '-DUSE_BLAS_LIB',
                                               '-std=c++11'],
                           language='c++',
                           depends=['spams_wrap/spams.h'])

    return [spams_wrap]


def mkhtml(d=None, base='sphinx'):
    if d is None:
        d = base
    else:
        d = os.path.join(base, d)
    if not os.path.isdir(base):
        return []
    hdir = d

    l1 = os.listdir(hdir)
    l = []
    for s in l1:
        s = os.path.join(d, s)
        if not os.path.isdir(s):
            l.append(s)
    return l


long_description = """Python interface for SPArse Modeling Software (SPAMS),
an optimization toolbox for solving various sparse estimation problems."""

opts = dict(name='python-spams',
            version='2.6.1.3',
            description='Python interface for SPAMS',
            long_description=long_description,
            author='Julien Mairal',
            author_email='spams.dev@inria.fr',
            url='http://spams-devel.gforge.inria.fr/',
            license='GPLv3',
            setup_requires=['Cython>=0.29', 'numpy>=1.18.4'],
            install_requires=['Cython>=0.29', 'numpy>=1.18',
                              'Pillow>=6.2', 'scipy>=1.4', 'six>=1.15'],
            packages=find_packages(),
            cmdclass={'build_ext': CustomBuildExtCommand},
            ext_modules=get_extension(),
            data_files=[('tests', ['tests/test_spams.py',
                                   'tests/test_decomp.py',
                                   'tests/test_dictLearn.py',
                                   'tests/test_linalg.py',
                                   'tests/test_prox.py',
                                   'tests/test_utils.py']),
                        ('doc', ['doc/doc_spams.pdf']),
                        ('doc/sphinx/_sources',
                         mkhtml(d='_sources', base='doc/sphinx')),
                        ('doc/sphinx/_static', mkhtml(d='_static',
                                                      base='doc/sphinx')),
                        ('doc/sphinx', mkhtml(base='doc/sphinx')),
                        ('doc/html', mkhtml(base='doc/html')),
                        ('tests', ['data/boat.png', 'data/lena.png'])],
            include_package_data=True,
            zip_safe=True)

setup(**opts)
