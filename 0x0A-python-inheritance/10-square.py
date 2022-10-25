#!/usr/bin/python3
"""
This module implements a Square object
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """implementation
    """
    
    def __init__(self, size):
        """initialization
        Args:
            size (int): size
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
