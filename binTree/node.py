# coding: utf-8


class Node(object):
    """Класс узла """

    def __init__(self, data=None, left=None, right=None):
        if not right:
            right = []
        if not left:
            left = []
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node[' + str(self.data) + ']'

    def __repr__(self):
        return 'Node[' + str(self.data) + ']'
