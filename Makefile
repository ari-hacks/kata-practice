  
help:
	@echo "test - run tests"

python-test:
	cd tests/python_test
	pytest

go-test:
	cd tests/go_test
	go test