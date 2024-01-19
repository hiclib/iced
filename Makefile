PYTHON ?= python
PIP ?= pip
CYTHON ?= cython
PYTEST ?= pytest
CTAGS ?= ctags

all: clean inplace test

inplace: cython
	$(PYTHON) setup.py build_ext -i

install: cython
	python -m pip install .

test: test-code

test-code: inplace
	$(PYTEST) --showlocals -v iced --durations=20

test-coverage:
	rm -rf coverage .coverage
	$(PYTEST) iced --showlocals -v --cov=iced

clean-ctags:
	rm -f tags

clean: clean-ctags
	$(PYTHON) setup.py clean
	rm -rf dist
	rm -rf build

trailing-spaces:
	find iced -name "*.py" -exec perl -pi -e 's/[ \t]*$$//' {} \;

cython:
	find iced -name "*.pyx" -exec $(CYTHON) {} \;
