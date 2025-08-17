"""
test_app.py

Script to test app
"""

# Run the tests with: pytest tests/test_app.py
from app import add_numbers

def test_add_numbers():
    """ Unit test 1 """
    assert 3 == add_numbers(1,2)
