  
.PHONY: clean-pyc clean-build docs

help:
	@echo "test - run tests"

test:
	cd tests 
	pytest