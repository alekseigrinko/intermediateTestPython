from datetime import datetime

class Note:
    id = None
    head = ""
    description = ""
    timeCreate = datetime.now()
    timeUpdate = datetime.now()

    def __init__(self, number, head, description):
        self.id = number
        self.head = head
        self.description = description

    def printInFile(self):
        return f"{self.id} ; {self.head} ; {self.description} ; {self.timeCreate} ; {self.timeUpdate}"
    
    def printNote(self):
        return f"ID: {self.id} ; заголовок: {self.head} ; описание: {self.description} ; дата создания: {self.timeCreate} ; дата обновления: {self.timeUpdate}"
    
    def setTimeCreate(self, line: str):
        self.timeCreate = datetime.strptime(line[:len(line)-1], '%Y-%m-%d %H:%M:%S.%f')

    def setTimeUpdate(self, line: str):
        self.timeUpdate = datetime.strptime(line[:len(line)-2], '%Y-%m-%d %H:%M:%S.%f')
    
    def updateTime(self):
        self.timeUpdate = datetime.now()

    def setHead(self, line: str):
        self.head = line

    def setDescription(self, line: str):
        self.description = line
