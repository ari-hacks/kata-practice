GOCMD=go  
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOTEST=$(GOCMD) test
GOGET=$(GOCMD) get
PYTHONTEST= pytest



help:
	@echo "test - run tests"

python-test:
	cd tests/python_test
	$(PYTHONTEST)

go-test:
	cd katas/go/kyu$(n)
	$(GOTEST) -v ./...