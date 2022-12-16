# 12.3
class Node:
    __slots__ = ['__value', '__next']

    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

# 12.4
def print_node(node_seq):
    if node_seq == None:
        print(end = '')
    else:
        print(node_seq.get_value(), end = ', ')
        print_node(node_seq.get_next())
        