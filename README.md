
# SPAMS 2.6.1 and python

SPAMS (SPArse Modeling Software) is an optimization toolbox for solving various sparse estimation problems.

-   Dictionary learning and matrix factorization:
	- NMF
	- sparse PCA
-   Solving sparse decomposition problems:
	- LARS
	- coordinate descent
	- OMP
	- proximal methods
-   Solving structured sparse decomposition problems:
	- l1/l2
	- l1/linf
	- sparse group lasso
	- tree-structured regularization
	- structured sparsity with overlapping groups.

---

Author:
* Julien Mairal (Inria) with the collaboration of Francis Bach (Inria),
* Jean Ponce (Ecole Normale Supérieure),
* Guillermo Sapiro (University of Minnesota),
* Guillaume Obozinski (Inria),
* Rodolphe Jenatton (Inria).

Credit:
* R and Python interfaces by Jean-Paul Chieze (Inria).
* Archetypal analysis implementation by Yuansi Chen (internship at Inria) with the collaboration of Zaid Harchaoui.

Maintenance:
* Development and maintenance are done by Ghislain Durif (Inria).

Licence: GPL v3

---

Manipulated objects are imported from numpy and scipy. Matrices should be stored by columns, and sparse matrices should be "column compressed".

### Installation from PyPI:

The standard installation uses the BLAS and LAPACK libraries used by Numpy:
```bash
pip install spams-python
```

### Installation from sources

Make sure you have install libblas & liblapack (see below)
```bash
pip install -e .
```


### Testing the interface :
```bash
python tests/test_spams.py -h # to get help
python tests/test_spams.py  # will run all the tests
```

### Comments
Carefully install libblas & liblapack. For example on ubuntu, necessary to `sudo apt-get -y install libblas-dev liblapack-dev gfortran`
