class Node:
    __name = 1

    # is node blocked? Default: False
    def __init__(self, b=False):
        self.name = Node.__name
        self._blocked = b
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        Node.__name += 1

    def __str__(self):
        if (self.blocked):
            return '[X]'
        else:
            return '[O]'

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
    def blocked(self):
        return self._blocked

    @blocked.setter
    def blocked(self, val):
        if (isinstance(val, bool)):
            self._blocked = val
        else:
            raise TypeError("blocked can only be a boolean value")
