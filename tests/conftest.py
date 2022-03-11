import pytest

@pytest.fixture
def input_string():
    string = 'henry'
    return string


@pytest.fixture
def input_string2():
    string2 = 'dog'
    return string2

@pytest.fixture
def input_string3():
    string3 = '  hello world  '
    return string3