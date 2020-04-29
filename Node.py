class Node:
    def __init__(self, v, r=None, le= None):
        self.__val = v
        self.__right = r
        self.__left = le

    def getval(self):
        return self.__val

    def getright(self):
        return self.__right

    def getleft(self):
        return self.__left

    def setright(self, r):
        self.__right = r

    def setleft(self, r):
        self.__left = r

    def __str__(self):
        return self.getval()

if __name__ == '__main__':
    n = Node(1, 24, 5)
    no = Node(24, 36, 5)
    print(n.getleft(), n.getright(), n.getval())
    print(no.getleft(), no.getright(), no.getval())