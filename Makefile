PYTHON ?= python
CYTHON ?= cython
NOSETESTS ?= nosetests
CTAGS ?= ctags

all: clean inplace test

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
