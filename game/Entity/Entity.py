import os

class Entity:
    baseDir = os.path.abspath(os.getcwd())

    def __init__(self, worldPath, name) :
        self.worldPath = worldPath
        self.name = name

    def exists(self):
        path = os.path.abspath(self.baseDir+"/world/"+self.worldPath+"/"+self.name+".py")
        exist = os.path.isfile(path)
        return exist

    def create(self):
        path = os.path.abspath(self.baseDir+"/world/"+self.worldPath+"/"+self.name+".py")
        open(path,'a').close()

    def remove(self):
        path = os.path.abspath(self.baseDir+"/world/"+self.worldPath+"/"+self.name+".py")
        if os.path.isfile(path):
            os.remove(path)