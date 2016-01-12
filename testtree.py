# coding: utf-8
from binTree.tree import Tree


def t_join():
    tr = Tree()
    tr2 = Tree()

    for x in range(100):
        tr.insertrndroot(x, tr.root)

    for x in range(200, 300):
        tr2.insertrndroot(x, tr2.root)
    return tr, tr2


def t_remove():
    tr = Tree()
    for x in range(49, 60):
        tr.insertrndroot(x, tr.root)
    print r"=====Старт Теста на удаление===="
    print r"Выводим созданное дерево до удаления"
    print tr.printlevelorder()
    print r"Всего узлов"
    print tr.sizenode(tr.root)
    print tr.remove(tr.root, 50)
    print r"узлов после удаления"
    print tr.sizenode(tr.root)
    print r"Дерево после удаления"
    print tr.printlevelorder()
