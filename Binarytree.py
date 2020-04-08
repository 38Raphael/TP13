from Node import Node


class Binarytree:
    def __init__(self, r):
        self.__root = r

    def getroot(self):
        return self.__root

if __name__ == '__main__':
    feuille1 = Node(21)
    feuille2 = Node(18)
    feuille3 = Node(3)
    feuille4 = Node(6)
    noeud1 = Node(19, feuille1, feuille2)
    noeud2 = Node(17, noeud1)
    noeud3 = Node(4, None, feuille3)
    noeud4 = Node(5, feuille4, noeud3)
    racine = Node(12, noeud2, noeud4)
    tree = Binarytree(racine)
