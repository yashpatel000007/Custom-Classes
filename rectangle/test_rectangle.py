import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rectangle.rectangle import Rectangle

def test_rectangle():
    rect = Rectangle(10, 5)
    for dimension in rect:
        print(dimension)

if __name__ == "__main__":
    test_rectangle()
