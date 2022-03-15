#!/bin/bash

# exit in case of any errors
set -e

################################################################################
# help                                                                         #
################################################################################
function print_help() {
    # Display Help
    echo "Build script for spams packages"
    echo
    echo "Usage: $0 [option...]"
    echo
    echo "   -h     Print the help"
    echo "   -v     Verbose mode"
    echo
    exit 1
}

################################################################################
# utils                                                                        #
################################################################################

# log with verbosity management
function logging() {
    if [[ ${PYBUILD_VERBOSE} == 1 ]]; then
        echo -e $1
    fi
}

################################################################################
# process script options                                                       #
################################################################################

# default options
PYBUILD_VERBOSE=0

# Get the options
while getopts 'hv' option; do
    case $option in
        h) # display Help
            print_help
            ;;
        v) # enable verbosity
            PYBUILD_VERBOSE=1
            logging "## verbose mode"
            ;;
        \?) # Invalid option
            echo "Error: Invalid option"
            exit 1
            ;;
    esac
done

################################################################################
# script setup                                                                 #
################################################################################

# project root directory
PROJDIR=$(git rev-parse --show-toplevel)

# python exec
PYTHON="python3"

# python environment for build
BUILD_VENV=${PROJDIR}/.build_venv

# python build requirements (names of packages to be installed with pip)
BUILD_REQ="pip build"

################################################################################
# prepare python environment                                                   #
################################################################################

logging "-- Preparing python environment for build..."

${PYTHON} -m venv --clear ${BUILD_VENV}
source ${BUILD_VENV}/bin/activate

logging "---- Python version = $(python -V)"

pip install -U ${BUILD_REQ}

################################################################################
# build spams                                                                  #
################################################################################

logging "-- Building spams..."

python -m build --sdist .
