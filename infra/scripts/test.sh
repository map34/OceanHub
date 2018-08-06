#!/usr/bin/env bash

set -e

if [[ $TEST_TARGET == 'test' ]]; then
    echo 'Perform simple test that environment is built' ;
    source activate TEST;
    python backend/server/manage.py test -n oceanhub;
fi
