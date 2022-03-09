# SPAMS: a SPArse Modeling Software

Here is the Python package interfacing the SPAMS C++ library.

## What is SPAMS?

SPAMS (SPArse Modeling Software) is an optimization toolbox for solving various sparse estimation problems.

- Dictionary learning and matrix factorization (NMF, sparse PCA, ...)
- Solving sparse decomposition problems with LARS, coordinate descent, OMP, SOMP, proximal methods
- Solving structured sparse decomposition problems (l1/l2, l1/linf, sparse group lasso, tree-structured regularization, structured sparsity with overlapping groups, ...)


## Installation

### Requirements

- a C++ modern compiler (tested with gcc >= 4.5)
- a BLAS/LAPACK library (like OpenBLAS, Intel MKL, Atlas)

Carefully install **libblas & liblapack**. For example, on Ubuntu, it is necessary to do `sudo apt-get -y install libblas-dev liblapack-dev gfortran`. For MacOS, you most likely need to do `brew install gcc openblas lapack`.

For better performance, we recommend to install the **MKL Intel library** (available for instance on PyPI with `pip install mkl`, or in the Anaconda Python distribution with `conda install mkl`) before installing Numpy (which is a dependency of SPAMS, the latter checking Numpy configuration for its installation).

SPAMS for Python was tested on **Linux** and **MacOS**. It is **not available for Windows** at the moment. **For MacOS users**, the install setup detects if OpenMP is available on your system and enable/disable OpenMP support accordingly. For better performance, we recommend to install an **OpenMP-compatible compiler** on your system (e.g. `gcc` or `llvm`).

**Note for Windows users:** at the moment you can run `pip install spams-bin` (provided by <https://github.com/samuelstjean/spams-python>).

### Installation from PyPI:

The standard installation uses the BLAS and LAPACK libraries used by Numpy:
```bash
pip install spams
```

### Installation from sources

Make sure you have install libblas & liblapack (see above)
```bash
git clone https://github.com/getspams/spams-python
cd spams-python
pip install -e .
```

### Usage

Manipulated objects are imported from numpy and scipy. Matrices should be stored by columns, and sparse matrices should be "column compressed".


### Testing the interface

- From the command line (to be called from the project root directory):
```bash
python tests/test_spams.py -h       # print the man page
python tests/test_spams.py          # run all the tests
```

- From Python (assuming `spams` package is installed):
```python
from spams.tests import test_spams

test_spams('-h')                    # print the man page
test_spams()                        # run all tests
test_spams(['sort', 'calcAAt'])     # run specific tests
test_spams(python_exec='python3')   # specify the python exec
```

- From the command line (assuming `spams` package is installed):
```bash
# c.f. previous point for the different options
python -c "from spams.tests import test_spams; test_spams()"
```

---

## Links

- [Official website](https://thoth.inrialpes.fr/people/mairal/spams/) (documentation and downloads)
- [Python specific project](https://github.com/getspams/spams-python) and [PyPI](https://pypi.org/project/spams/) repository (available with `pip install spams`)
- [R specific project](https://github.com/getspams/spams-R) (available with `remotes::install_github("getspams/spams-R")`)
- [Original C++ project](https://github.com/getspams/spams-devel) (and original sources for Matlab, Python and R interfaces)

> SPAMS-related git repositories are also available on [Inria](https://www.inria.fr/) [gitlab forge](https://gitlab.inria.fr/): see [original C++ project](https://gitlab.inria.fr/thoth/spams-devel)  (and original sources for Matlab, Python and R interfaces), [Python specific project](https://gitlab.inria.fr/thoth/python-spams)


## Contact

Regarding SPAMS **Python** package: you can open an issue on the dedicated git project at <https://github.com/getspams/spams-python>

Regarding SPAMS **R** package: you can open an issue on the dedicated git project at <https://github.com/getspams/spams-R>

For any other question related to the use or development of SPAMS:

- you can you can contact us at `spams.dev'AT'inria.fr` (replace `'AT'` by `@`)
- you can open an issue on the general git project at <https://github.com/getspams/spams-devel>

---

## Authorship

SPAMS is developed and maintained by [Julien Mairal](http://julien.mairal.org) (Inria), and contains sparse estimation methods resulting from collaborations with various people: notably, [Francis Bach](http://www.di.ens.fr/~fbach), [Jean Ponce](http://www.di.ens.fr/~ponce), Guillermo Sapiro, [Rodolphe Jenatton](http://www.di.ens.fr/~jenatton/) and [Guillaume Obozinski](http://imagine.enpc.fr/~obozinsg/).

It is coded in C++ with a Matlab interface. Interfaces for R and Python have been developed by Jean-Paul Chieze, and archetypal analysis was written by Yuansi Chen.

Release of version 2.6/2.6.1 and porting to R-3.x and Python3.x was done by [Ghislain Durif](https://gdurif.perso.math.cnrs.fr/) (Inria). The original porting to Python3.x is based on [this patch](https://aur.archlinux.org/packages/python-spams-svn/) and on the work of John Kirkham available [here](https://github.com/conda-forge/python-spams-feedstock).

Version 2.6.2 (Python only) update is based on contributions by [Francois Rheault](https://github.com/frheault) and [Samuel Saint-Jean](http://samuelstjean.github.io/).

### Maintenance

Since version 2.6.3+, SPAMS (especially the Python version) is now maintained by the following team:

- [Alessandro Daducci](https://github.com/daducci)
- [Ghislain Durif](https://gdurif.perso.math.cnrs.fr/)
- [Francois Rheault](https://github.com/frheault)
- [Samuel Saint-Jean](http://samuelstjean.github.io/)

---

## Funding

This work was supported in part by the SIERRA and VIDEOWORLD ERC projects, and by the MACARON ANR project.

## License

Version 2.1 and later are open-source under [GPLv3 licence](http://www.gnu.org/licenses/gpl.html). For other licenses, please contact the authors.

---

## News

- 14/02/2022: Python SPAMS is now officially hosted on [Github](https://github.com/getspams/spams-python)
- 07/02/2022: [SPAMS C++ project](https://github.com/getspams/spams-devel) and [SPAMS for R](https://github.com/getspams/spams-R) are now officially hosted on Github
- 03/02/2022: Python SPAMS v2.6.3 is released (source and PyPI)
- 03/09/2020: Python SPAMS v2.6.2 is released (source and PyPI)
- 15/01/2019: Python SPAMS v2.6.1 is available on PyPI)
- 08/12/2017: Python SPAMS v2.6.1 for Anaconda (with MKL support) is released
- 24/08/2017: Python SPAMS v2.6.1 is released (a single source code for Python 3 and 2)
- 27/02/2017: SPAMS v2.6 is released, including precompiled Matlab packages, R-3.x and Python3.x compatibility
- 25/05/2014: SPAMS v2.5 is released
- 12/05/2013: SPAMS v2.4 is released
- 05/23/2012: SPAMS v2.3 is released
- 03/24/2012: SPAMS v2.2 is released with a Python and R interface, and new compilation scripts for a better Windows/Mac OS compatibility
- 06/30/2011: SPAMS v2.1 goes open-source!
- 11/04/2010: SPAMS v2.0 is out for Linux and Mac OS!
- 02/23/2010: Windows 32 bits version available! Elastic-Net is implemented
- 10/26/2009: Mac OS, 64 bits version available!

---

## References

### A monograph about sparse estimation

We encourage the users of SPAMS to read the following monograph, which contains numerous applications of dictionary learning, an introduction to sparse modeling, and many practical advices.

- J. Mairal, F. Bach and J. Ponce. [Sparse Modeling for Image and Visio Processing](http://lear.inrialpes.fr/people/mairal/resources/pdf/review_sparse_arxiv.pdf). Foundations and Trends in Computer Graphics and Vision. vol 8. number 2-3. pages 85--283. 2014

### Related publications

You can find here some publications at the origin of this software.

The "matrix factorization" and "sparse decomposition" modules were developed for the following papers:

- J. Mairal, F. Bach, J. Ponce and G. Sapiro. [Online Learning for Matrix Factorization and Sparse Coding](https://www.jmlr.org/papers/volume11/mairal10a/mairal10a.pdf). Journal of Machine Learning Research, volume 11, pages 19-60. 2010.
- J. Mairal, F. Bach, J. Ponce and G. Sapiro. [Online Dictionary Learning for Sparse Coding](http://www.di.ens.fr/willow/pdfs/icml09.pdf). International Conference on Machine Learning, Montreal, Canada, 2009

The "proximal" module was developed for the following papers:

- J. Mairal, R. Jenatton, G. Obozinski and F. Bach. [Network Flow Algorithms for Structured Sparsity](http://books.nips.cc/papers/files/nips23/NIPS2010_1040.pdf). Adv. Neural Information Processing Systems (NIPS). 2010.
- R. Jenatton, J. Mairal, G. Obozinski and F. Bach. [Proximal Methods for Sparse Hierarchical Dictionary Learning](http://www.di.ens.fr/willow/pdfs/icml2010a.pdf). International Conference on Machine Learning. 2010.

The feature selection tools for graphs were developed for:

- J. Mairal and B. Yu. [Supervised Feature Selection in Graphs with Path Coding Penalties and Network Flows](http://arxiv.org/abs/1204.4539). JMLR. 2013.

The incremental and stochastic proximal gradient algorithm correspond to the following papers:

- J. Mairal. [Stochastic Majorization-Minimization Algorithms for Large-Scale Optimization](http://hal.inria.fr/docs/00/86/02/68/PDF/main_with_appendices.pdf). NIPS. 2013.
- J. Mairal. [Optimization with First-Order Surrogate Functions](http://hal.inria.fr/docs/00/82/22/29/PDF/main.pdf). International Conference on Machine Learning. 2013.
