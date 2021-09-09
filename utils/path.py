import os
class Path:
    def __init__(self) -> None:
        pass
    def getDataPath(self):
        return str(os.path.abspath(os.path.join('../data')))
# paths = Path()
# print(Path.getDataPath)