class FileLoader:
    def __init__(self):
        self.filesList = []

    def addFileInList(self, filepath, entityType):
        self.filesList.append({entityType: filepath})

    def loadJsonFile(self, filepath):
        print('todo')


