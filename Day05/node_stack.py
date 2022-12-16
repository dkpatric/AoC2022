import node

# 12.5
class Stack:
    __slots__ = ['__size', '__top']

    def __init__(self):
        self.__size = 0
        self.__top = None

    def size(self):
        return self.__size

    def is_empty(self):
        #  return self.__size == 0
        return self.__top == None

    # 12.6
    def __stringify(self, node):
        if node == None:
            return ''
        else:
            return self.__stringify(node.get_next()) + \
                str(node.get_value()) + ', '

    def __repr__(self):
        string = self.__stringify(self.__top)
        return '[' + string[:-2] + ']'

    # 12.7
    def push(self, value):
        new_node = node.Node(value, self.__top)
        self.__top = new_node
        self.__size += 1

    # 12.8
    def peek(self):
        return self.__top.get_value()

    # 12.9
    def pop(self):
        value = self.__top.get_value()
        self.__top = self.__top.get_next()
        self.__size -= 1
        return value