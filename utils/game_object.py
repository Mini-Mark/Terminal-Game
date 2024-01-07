class Position:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def updatePosition(self, x, y):
        self._x = x
        self._y = y

    def moveUp(self): self._y -= 1
    def moveDown(self): self._y += 1
    def moveLeft(self): self._x -= 1
    def moveRight(self): self._x += 1

    def getX(self): return self._x
    def getY(self): return self._y


class GameObject(Position):
    def __init__(self, name, position):
        super().__init__(position[0], position[1])

        self._name = name

    def getName(self):
        return self._name
