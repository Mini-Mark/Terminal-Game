import settings.config as config


class Area:
    def __init__(self, topSpace=0, bottomSpace=0, titleLabel="", actionLabel=""):
        self._titleLabel = titleLabel
        self._actionLabel = actionLabel
        self._topSpace = topSpace
        self._bottomSpace = bottomSpace
        self._setup()

    def _setup(self):
        self._width = config.AREA_SIZE_WIDTH - 3
        self._height = config.AREA_SIZE_HEIGHT - 2
        self._area = []
        self._mapObject = []

        self._area.append(config.BORDER_ALPHABET_VERTICAL *
                          (config.AREA_SIZE_WIDTH + 1))
        for i in range(0, config.AREA_SIZE_HEIGHT + 1 - 2):
            self._area.append(
                f"{config.BORDER_ALPHABET_HORIZONTAL}{' ' * (config.AREA_SIZE_WIDTH + 1 - 2)}{config.BORDER_ALPHABET_HORIZONTAL}")
        self._area.append(config.BORDER_ALPHABET_VERTICAL *
                          (config.AREA_SIZE_WIDTH + 1))

    def show(self):
        print(" " * self._topSpace)
        print(self._titleLabel)

        tempArea = self._area.copy()

        for obj in self._mapObject:
            tempArea[obj.getY() + 1] = tempArea[obj.getY() +
                                                1][:(obj.getX() + 1)] + obj.getName() + tempArea[obj.getY() + 1][(obj.getX() + 1 + len(obj.getName())):]

        print("\n".join(tempArea), end="")
        print(f"\n{self._actionLabel}", end="")
        print(" " * self._bottomSpace)

    def addObjectToArea(self, obj):
        self._mapObject.append(obj)

    def clear(self):
        self._setup()

    def setTitleLabel(self, label): self._titleLabel = label
    def setActionLabel(self, label):  self._actionLabel = label

    def getWidth(self): return self._width
    def getHeight(self): return self._height
