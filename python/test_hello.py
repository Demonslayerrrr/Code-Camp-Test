from python.main import hello_function
import pytest

def test_hello_function():
    assert hello_function() == "hello"
