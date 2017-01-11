#!/bin/bash
# This script is meant to be called by the "script" step defined in
# .travis.yml. See http://docs.travis-ci.com/ for more details.
# The behavior of the script is controlled by environment variabled defined
# in the .travis.yml in the top level folder of the project.

# License: 3-clause BSD

set -e

python --version
python -c "import numpy; print('numpy %s' % numpy.__version__)"
python -c "import scipy; print('scipy %s' % scipy.__version__)"
python -c "\
try:
    import pandas
    print('pandas %s' % pandas.__version__)
except ImportError:
    pass
"

python -c "import multiprocessing as mp; print('%d CPUs' % mp.cpu_count())"

run_tests(){
  # Get into a temp directory to run test from the installed iced and
  # check if we do not leave artifacts
  mkdir -p $TEST_DIR
  # We need the setup.cfg for the nose settings
  cp setup.cfg $TEST_DIR
  cd $TEST_DIR



  if [[ "$COVERAGE" == "TRUE" ]]; then
    nosetests -s --with-coverage iced
  else
    nosetests -s iced
  fi

  # Is directory still empty ?
  ls -ltra

  # Test doc
  cd $CACHED_BUILD_DIR/iced
  make test-doc test-sphinxext

}


if [[ "$RUN_FLAKE8" == "true" ]]; then
    source build_tools/travis/flake8_diff.sh
fi

if [[ "$SKIP_TESTS" != "true" ]]; then
    run_tests
fi
