import os

class Entity:
    def __init__(self, worldPath, name) :
        self.worldPath = worldPath
        self.name = name

    def exists(self):
        path = os.path.abspath("./world/"+self.worldPath+"/"+self.name+".py")
        exist = os.path.isfile(path)
        return exist