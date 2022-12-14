#!/usr/bin/python3
""" this module containg files that describe """

class Node:
    """ class node """
    def __init__(self, data, next_node=None):
        """ init funcion """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ define data """
        return self.__data

    @data.setter
    def data(self, value):
        """ data setter """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ next node """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ singly linked list """
    def __str__(self):
        """ return string reperesantion """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """ Initialize init """
        self.__head = None

    def sorted_insert(self, value):
        """ sorted insert """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
