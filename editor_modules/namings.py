from enum import Enum, auto

class ModeName(Enum):
    SETUP = auto()
    EDITOR = auto()

class MenuName(Enum):
    TILEGRID = auto()
    TILESET = auto()
    LAYERS = auto()
