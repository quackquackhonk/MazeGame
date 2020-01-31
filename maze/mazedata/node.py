class Node:
    _name = 1

    # is node blocked? Default: False
    def __init__(self, x, y):
        self.name = Node._name
        self.loc = (x, y)
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        Node._name += 1

    def __str__(self):
        return "[ ]"

    def __eq__(self, other):
        if (isinstance(other, self.__class__)):
            return self.name == other.name
        else:
            return False

    def setAbove(self, above):
        self.up = above
        above.down = self

    def setBelow(self, below):
        self.down = below
        below.up = self

    def setLeft(self, toLeft):
        self.left = toLeft
        toLeft.right = self

    def setRight(self, toRight):
        self.right = toRight
        toRight.left = self

    @property
    def neighbors(self):
        n = []
        if (self.up is not None):
            n.append(self.up)
        if (self.down is not None):
            n.append(self.down)
        if (self.left is not None):
            n.append(self.left)
        if (self.right is not None):
            n.append(self.right)
        return n


if __name__ == '__main__':
    pass
