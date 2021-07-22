#!/usr/bin/env bash
set -ex
            
export PIP_DEFAULT_TIMEOUT=60

if [[ $MINIMUM_REQUIREMENTS == 1 ]]; then
    for filename in requirements/*.txt; do
        sed -i 's/>=/==/g' $filename
    done
fi

python -m pip install --upgrade pip wheel setuptools
python -m pip install $PIP_FLAGS -r requirements/default.txt
python -m pip install $PIP_FLAGS -r requirements/tests.txt

set +ex
