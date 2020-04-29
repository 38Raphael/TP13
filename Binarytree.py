from Node import Node


class Binarytree:
    def __init__(self, r):
        self.__root = r

    def getroot(self):
        return self.__root

    def isroot(self, node):
        return True if node == self.__root else False

    def size(self, node):
        if node.getleft() is None:
            if node.getright() is None:
                return 1
        if node.getright() is None and node.getleft() is not None:
            return 1 + self.size(node.getleft())
        elif node.getleft() is None and node.getright() is not None:
            return 1 + self.size(node.getright())
        elif node.getright() and node.getleft() is not None:
            return 1 + self.size(node.getright()) + self.size(node.getleft())

    def printvalues(self, node):
        if node.getleft() is None:
            if node.getright() is None:
                return str(node.getval())
        if node.getright() is None and node.getleft() is not None:
            return str(node.getval()) + " " + self.printvalues(node.getleft())
        elif node.getleft() is None and node.getright() is not None:
            return str(node.getval()) + " " + self.printvalues(node.getright())
        elif node.getright() and node.getleft() is not None:
            return str(node.getval()) + " " + self.printvalues(node.getright()) + " " + self.printvalues(node.getleft())

    def sumvalues(self, node):
        if node.getleft() is None:
            if node.getright() is None:
                return node.getval()
        if node.getright() is None and node.getleft() is not None:
            return node.getval() + self.sumvalues(node.getleft())
        elif node.getleft() is None and node.getright() is not None:
            return node.getval() + self.sumvalues(node.getright())
        elif node.getright() and node.getleft() is not None:
            return node.getval() + self.sumvalues(node.getright()) + self.sumvalues(node.getleft())

    def numberleaves(self, node):
        if node.getleft() is None:
            if node.getright() is None:
                return 1
        if node.getright() is None and node.getleft() is not None:
            return self.numberleaves(node.getleft())
        elif node.getleft() is None and node.getright() is not None:
            return self.numberleaves(node.getright())
        elif node.getright() and node.getleft() is not None:
            return self.numberleaves(node.getright()) + self.numberleaves(node.getleft())

    def numberinternalnodes(self, node):
        return self.size(node) - self.numberleaves(node)

    def height(self, node):
        if node is None:
            return 0
        if node.getright() is None and node.getleft() is None:
            return 1 if self.isroot(node) is True else 0
        else:
            hauteurNoeuddroite = 1 + self.height(node.getright())
            hauteurNoeudgauche = 1 + self.height(node.getleft())
        hauteurNoeud = max(hauteurNoeuddroite,hauteurNoeudgauche)
        return hauteurNoeud

    def belongs(self, node, val):
        if node is not None:
            if node.getval() is val:
                return True
            elif self.belongs(node.getleft(), val) is not True:
                return self.belongs(node.getright(), val)
            elif self.belongs(node.getright(), val) is not True:
                return self.belongs(node.getleft(), val)
        else:
            return

    def ancestors(self, node, val):




if __name__ == '__main__':
    # Création de l'arbre
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
    # Utilisation de la classe
    print(tree.size(tree.getroot()))
    print(tree.printvalues(tree.getroot()))
    print(tree.sumvalues(tree.getroot()))
    print(tree.numberleaves(tree.getroot()))
    print(tree.numberinternalnodes(tree.getroot()))
    print(tree.height(tree.getroot()))
    print(tree.belongs(tree.getroot(), 54))
