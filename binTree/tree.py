# coding: utf-8
from .node import Node
import copy
import random


class Tree(object):
    """Класс дерева"""

    def __init__(self, root=None):
        if not root:
            self.root = []  # корень дерева
        else:
            self.root = root

    def __str__(self):
        return r"Tree with " + str(self.sizenode(self.root)) + r" Nodes"

    def __repr__(self):
        return r"Tree with " + str(self.sizenode(self.root)) + r" Nodes"

    @staticmethod
    def newnode(data, left=None, right=None):
        if not left:
            left = []
        if not right:
            right = []
        return Node(data, left, right)

    def height(self, nodes, ind=0):
        """
        Высота дерева
        :param nodes:
        :param ind:
        :return:
        """
        try:
            if not nodes[ind]:
                return 0
        except IndexError:
            if not nodes:
                return 0

        else:
            lheight = self.height(nodes[ind].left, ind)
            rheight = self.height(nodes[ind].right, ind)

            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def mirrortree(self, nodes, ind=0):
        """
        Зеркальное отражение дерева
        :param nodes:
        :param ind:
        :return:
        """
        if nodes[ind].left and nodes[ind].right:
            nodes[ind].left, nodes[ind].right = nodes[ind].right, nodes[ind].left
            self.mirrortree(nodes[ind].right)
            self.mirrortree(nodes[ind].left)
        else:
            if nodes[ind].left == [] and nodes[ind].right:
                return self.mirrortree(nodes[ind].right)
            if nodes[ind].right == [] and nodes[ind].left:
                return self.mirrortree(nodes[ind].left)

    def lookup(self, nodes, target, ind=0):
        """
        Поиск по дереву
        :param nodes:
        :param target:
        :param ind:
        :return:
        """
        try:
            if not nodes[ind]:
                return 0
            else:
                if target == nodes[ind].data:
                    return 1
                else:
                    if target < nodes[ind].data:
                        return self.lookup(nodes[ind].left, target, ind)
                    else:
                        return self.lookup(nodes[ind].right, target, ind)
        except IndexError:
            if not nodes:
                return 0
            else:
                return "Index Error(la)"

    def getmaxwidth(self, root, ind=0):
        """
        Ширина дерева максимальная
        :param root:
        :param ind:
        :return:
        """
        maxwdth = 0
        i = 1

        h = self.height(root, ind)
        while i < h:
            width = self.getwidth(root, i, ind)
            if width > maxwdth:
                maxwdth = width
            i += 1
        return maxwdth

    def getwidth(self, root, level, ind=0):
        """
        Ширина уровня дерева
        :param root:
        :param level:
        :param ind:
        :return:
        """
        try:
            if not root[ind]:
                return 0
        except IndexError:
            if root:
                return "Index Error(gw)"
            else:
                return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.getwidth(root[ind].left, level - 1, ind) + self.getwidth(root[ind].right, level - 1, ind)

    def printgivenlevel(self, root, level, ind=0):
        """Распечатка уровня дерева
        :param root:
        :param level:
        :param ind:
        """
        try:
            if not root[ind]:
                return None
        except IndexError:
            if not root:
                return None
            else:
                return "Index Error(pl)"
        if level == 1:
            print "%d " % root[ind].data,
        elif level > 1:
            self.printgivenlevel(root[ind].left, level - 1, ind)
            self.printgivenlevel(root[ind].right, level - 1, ind)

    def printlevelorder(self, ind=0):
        """Распечатка дерева
        :param ind:
        """
        h = self.height(self.root, ind)
        i = 1
        while i <= h:
            self.printgivenlevel(self.root, i, ind)
            print
            print r"|||||"
            i += 1

    def sizenode(self, nodes, ind=0):
        """Кол во узлов
        :param ind:
        :param nodes:
        """
        try:
            if not nodes[ind]:
                return 0
        except IndexError:
            if not nodes:
                return 0
            else:
                return "Index Error(sn)"
        return self.sizenode(nodes[ind].left) + 1 + self.sizenode(nodes[ind].right)

    def addnode(self, data, root, ind=0):
        """Добавление узла
        :param data:
        :param root:
        :param ind:
        """
        try:
            if not root[ind]:
                root.append(self.newnode(data))
                return 1
        except IndexError:
            root.append(self.newnode(data))
            return 1
        try:
            if root[ind].data == data:
                return 0
        except IndexError:
            return r'Index Error(an)'
        if data > root[ind].data:
            return self.addnode(data, root[ind].right, ind)
        if data < root[ind].data:
            return self.addnode(data, root[ind].left, ind)

    @staticmethod
    def roteteright(nodes, ind=0):
        """
        Поворот на право
        :param nodes:
        :param ind:
        :return:
        """
        try:
            if not nodes[ind].left:
                return 0
        except IndexError:
            if nodes:
                return r"Index Error(rr)"
            else:
                return 0
        g = copy.deepcopy(nodes[ind].left)
        nodes[ind].left = copy.deepcopy(g[ind].right)
        g[ind].right = copy.deepcopy(nodes)
        nodes[ind] = copy.deepcopy(g[ind])
        return 1

    @staticmethod
    def roteteleft(nodes, ind=0):
        """
        Поворот на лево
        :param nodes:
        :param ind:
        :return:
        """
        try:
            if not nodes[ind].right:
                return 0
        except IndexError:
            if nodes:
                return r"Index Error(rl)"
            else:
                return 0
        g = copy.deepcopy(nodes[ind].right)
        nodes[ind].right = copy.deepcopy(g[ind].left)
        g[ind].left = copy.deepcopy(nodes)
        nodes[ind] = copy.deepcopy(g[ind])
        return 1

    def addnoderoot(self, data, root, ind=0):
        """Добавление узла в корень
        :param data:
        :param root:
        :param ind:
        """
        try:
            if not root[ind]:
                root.append(self.newnode(data))
                return 1
        except IndexError:
            root.append(self.newnode(data))
            return 1
        try:
            if root[ind].data == data:
                return 0
        except IndexError:
            return r'Index Error(anr)'
        if data > root[ind].data:
            self.addnoderoot(data, root[ind].right, ind)
            self.roteteleft(root, ind)
            return 1
        if data < root[ind].data:
            self.addnoderoot(data, root[ind].left, ind)
            self.roteteright(root, ind)
            return 1

    def insertrndroot(self, data, root, ind=0):
        """
        Рандомизированная вставка узла в дерево.
        :param data:
        :param root:
        :param ind:
        :return:
        """
        try:
            if not root[ind]:
                root.append(self.newnode(data))
                return 1
        except IndexError:
            root.append(self.newnode(data))
            return 1
        try:
            if root[ind].data == data:
                return 0
        except IndexError:
            return r'Index Error(irndr)'
        if random.randint(0, 32767) % (self.sizenode(root, ind) + 1) == 0:
            return self.addnoderoot(data, root, ind)
        if data > root[ind].data:
            return self.addnode(data, root[ind].right, ind)
        if data < root[ind].data:
            return self.addnode(data, root[ind].left, ind)

    def join(self, roota, rootb, ind=0):
        """
        Объединение узлов
        :param roota:
        :param rootb:
        :param ind:
        :return:
        """
        if not roota:
            return rootb
        if not rootb:
            return roota
        if random.randint(0, 32767) % (self.sizenode(roota, ind) + self.sizenode(rootb, ind)) < self.sizenode(
                roota, ind):
            roota[ind].right = copy.deepcopy(self.join(roota[ind].right, rootb, ind))
            return roota
        else:
            rootb[ind].left = copy.deepcopy(self.join(roota, rootb[ind].left, ind))
            return rootb

    def remove(self, nodes, data, ind=0):
        """
        Удаление узлов
        :param nodes:
        :param data:
        :param ind:
        :return:
        """
        if not (self.lookup(self.root, data, ind)):
            return 0
        if nodes[ind].data == data:
            nodes[ind] = (copy.deepcopy(self.join(nodes[ind].left, nodes[ind].right, ind)))[ind]
            return 1
        elif data < nodes[ind].data:
            return self.remove(nodes[ind].left, data, ind)
        else:
            return self.remove(nodes[ind].right, data, ind)
