import pytest

# @pytest.fixture
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        print('executed')
    return wrapper_do_twice

# @pytest.fixture
def decorate(str):
    return f'## {str} ##'
