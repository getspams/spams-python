import os
# import platform
import sys

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

from distutils.sysconfig import get_python_inc
# from distutils.util import get_platform

def check_openmp():
    # see https://stackoverflow.com/questions/16549893/programatically-testing-for-openmp-support-from-a-python-setup-script/16555458#16555458
    import os, tempfile, textwrap, subprocess, shutil

    # see http://openmp.org/wp/openmp-compilers/
    omp_test = textwrap.dedent(
        r"""
        #include <omp.h>
        #include <stdio.h>
        int main() {
        #pragma omp parallel
        printf("Hello from thread %d over %d\n", omp_get_thread_num(), omp_get_num_threads());
        }
        """
    )

    try:
        tmpdir = tempfile.mkdtemp()
        filename = r'test.c'
        with open(os.path.join(tmpdir, filename), 'w') as file:
            file.write(omp_test)
        with open(os.devnull, 'w') as fnull:
            result = subprocess.call(
                ['cc', '-fopenmp' ,'-o',
                 os.path.join(tmpdir, "exec"),
                 os.path.join(tmpdir, filename)],
                stdout=fnull, stderr=fnull
            )
    except:
        result = 1
    finally:
        shutil.rmtree(tmpdir)
    # output : 0 if ok, 1 if not
    return result

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

    # blas/lapack compile/linking info
    try:
        blas_opt_info = np.__config__.blas_opt_info
    except:
        try:
            blas_opt_info = np.__config__.blas_ilp64_opt_info
        except:
            blas_opt_info = None

    try:
        lapack_opt_info = np.__config__.lapack_opt_info
    except:
        try:
            lapack_opt_info = np.__config__.bla_ilp64_opt_info
        except:
            lapack_opt_info = None

    # blas extra compile args
    if blas_opt_info is not None:
        for _ in blas_opt_info.get('extra_compile_args', []):
            if _ not in cc_flags:
                cc_flags.append(_)

    # lapack extra compile args
    if lapack_opt_info is not None:
        for _ in lapack_opt_info.get('extra_compile_args', []):
            if _ not in cc_flags:
                cc_flags.append(_)

    # linking flags
    link_flags = []

    # blas extra linking flags
    if blas_opt_info is not None:
        for _ in blas_opt_info.get('extra_link_args', []):
            if _ not in link_flags:
                link_flags.append(_)

    # lapack extra linking flags
    if lapack_opt_info is not None:
        for _ in lapack_opt_info.get('extra_link_args', []):
            if _ not in link_flags:
                link_flags.append(_)

    # libs
    libs = ['stdc++']

    # mkl ?
    is_mkl = False
    if blas_opt_info is not None:
        for lib in blas_opt_info.get('libraries', []):
            if 'mkl' in lib:
                is_mkl = True
                break

    libdirs = np.distutils.system_info.blas_info().get_lib_dirs()
    if is_mkl:
        for _ in blas_opt_info.get('include_dirs', []):
            if _ not in incs:
                incs.append(_)
        for _ in blas_opt_info.get('library_dirs', []):
            if _ not in libdirs:
                libdirs.append(_)
        libs.extend(['mkl_rt'])
    else:
        libs.extend(['blas', 'lapack'])

    # openMP
    if check_openmp() == 0:
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


# project root directory
this_directory = os.path.abspath(os.path.dirname(__file__))

# version number
with open(os.path.join(this_directory, "version"), encoding="utf-8") as v:
    current_version = v.read().rstrip()

# package description
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# setup config
opts = dict(
    name='spams',
    version=current_version,
    description='Python interface for SPAMS',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Julien Mairal',
    author_email='spams.dev@inria.fr',
    url='https://thoth.inrialpes.fr/people/mairal/spams/',
    project_urls={
        "Bug Reports": "https://github.com/getspams/spams-python/issues",
        "Source": "https://github.com/getspams/spams-python",
    },
    license='GPLv3',
    python_requires='>=3',
    install_requires=['Cython>=0.29', 'numpy>=1.12',
                      'Pillow>=6.0', 'scipy>=1.0', 'six>=1.12'],
    packages=['myscipy_rand', 'spams_wrap', 'spams', 'spams.tests'],
    cmdclass={'build_ext': CustomBuildExtCommand},
    ext_modules=get_extension(),
    package_data={
        "spams": ["data/*.png", "version"]
    },
    zip_safe=True
)

setup(**opts)
