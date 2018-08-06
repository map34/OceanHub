#!/usr/bin/env bash

set -e

if [[ $TEST_TARGET == 'lint' ]]; then
    echo 'Perform simple lint that environment is built' ;
    source activate TEST;
    flake8 .;
fi
