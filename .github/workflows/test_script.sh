#!/usr/bin/env bash
# Fail on non-zero exit and echo the commands
set -ev

python -m pip list

(cd .. && pytest --doctest-modules --cov=iced --pyargs iced)
flake8 --exit-zero iced examples

(cd examples/HiC-pro && source launch_tests.sh)
set +ev
