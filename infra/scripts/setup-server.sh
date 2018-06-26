#!/usr/bin/env bash

URL="http://bit.ly/miniconda"
TRAVIS_PYTHON_VERSION=3.6

if [ ! -f $HOME/miniconda/bin/conda ] ; then
    echo "Fresh miniconda installation."
    wget $URL -O miniconda.sh
    rm -rf $HOME/miniconda
    bash miniconda.sh -b -p $HOME/miniconda
fi

export PATH="$HOME/miniconda/bin:$PATH"

conda update conda --yes
conda config --set show_channel_urls true
conda config --add channels conda-forge --force
conda create --yes -n TEST python=$TRAVIS_PYTHON_VERSION --file backend/requirements.txt --file backend/requirements-dev.txt
