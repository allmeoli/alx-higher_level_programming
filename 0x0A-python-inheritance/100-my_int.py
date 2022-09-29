#!/usr/bin/python3
class MyInt(int):
    """ Class that inherits from class int"""
    

    def __init__(self, value):
    """Initialize value"""
    self.value = value

    def __eq__(self, other):
        """ Method that returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that returns == check """
        return int.__eq__(self, other)