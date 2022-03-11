import pytest
# from string_reverse import reverse_string

def reverse_string(string: str) -> str:
    return string[::-1]

def test_string(input_string):
    assert reverse_string(input_string) == 'yrneh'

def test_string(input_string2):
    assert reverse_string(input_string2) == 'god'

def test_string(input_string3):
    assert reverse_string(input_string3) == '  dlrow  olleh  '