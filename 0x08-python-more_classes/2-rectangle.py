#!/usr/bin/python3
""" A rectangle with """


class Rectangle:
    """ A rectangle with a width and height. """
    def __init__(self, width=0, height=0):
        """ (Rectangle, number, number) """

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ (Rectangle, number, number) """
        return self.__width

    @width.setter
    def width(self, value):
        """ (Rectangle, number, number) """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ (Rectangle, number, number) """
        return self.__height

    @height.setter
    def height(self, value):
        """ (Rectangle, number, number) """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ calculate the area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ calculate the perimeter of rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)
