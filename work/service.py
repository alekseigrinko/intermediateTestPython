from note import Note

class Servise:

    dictionary = {}
    id = 1

    def start(self):
        check = True
        while check:
            Servise.menu()
            line = input("Введите команду: ")
            if "add" in line:
                Servise.addNote()
            elif "get" in line:
                Servise.getNote()
            elif "update" in line:
                Servise.updateNote()
            elif "remove" in line:
                Servise.removeNote()
            elif "list" in line:
                print("Список записей: ")
                Servise.getAllNotes()
            elif "save" in line:
                Servise.save()
                print("Записи сохранены!")
            elif "load" in line:
                Servise.load()
                print("Записи загружены!")
            elif "exit" in line:
                print("Выход из приложения!")
                check = False
    
    def menu():
        print("---------------------------------------")
        print("Добро пожаловать в приложение заметок!")
        print("Для сохранения заметок введите add")
        print("Для получение данных по заметки введите get")
        print("Для обновление заметки введите update")
        print("Для удаления заметки введите remove")
        print("Для получния списка всех заметок введите list")
        print("Для сохранения всех заметок введите save")
        print("Для загрузки всех заметок введите load")
        print("Для выхода из приложения введите exit")
        print("---------------------------------------")

    def addNote():
        head = input("Введите заголовок заметки: ")
        description = input("Введите описание заметки: ")
        newNote = Note(Servise.id, head, description)
        Servise.dictionary[Servise.id] = newNote
        print("Запись успешно создана: ")
        print(f"{newNote.printNote()}")
        Servise.id += 1

    def updateNote():
        id = input("Введите номер ID записи для обновления: ")
        updateNote = None
        for Note in Servise.dictionary.values():
            if Note.id == id:
                updateNote = Note
                head = input("Введите новый заголовок заметки: ")
                description = input("Введите новое описание заметки: ")
                updateNote.setHead(head)
                updateNote.setDescription(description)
                updateNote.updateTime()
                Servise.dictionary[id] = updateNote
                print(f"Обновлена заметка {updateNote.printNote()}")
        if updateNote == None:
            print("Запись не найдена!")

    def removeNote():
        id = input("Введите номер ID записи для удаления: ")
        removeNote = None
        for Note in Servise.dictionary.values():
            if Note.id == id:
                removeNote = Note
        if removeNote == None:
            print("Запись не найдена!")
        else:
            Servise.dictionary.pop(id)
            print(f"Запись: {removeNote.printNote()}, удалена")
    
    def getNote():
        id = input("Введите номер ID записи: ")
        note = None
        for Note in Servise.dictionary.values():
            if Note.id == id:
                note = Note
        if note == None:
            print("Запись не найдена!")
        else:
            print(f"Запись: {note.printNote()}")
    
    def getAllNotes():
        for Note in Servise.dictionary.values():
            print(f"{Note.printNote()}")

    def save():
        f = open("notebook.csv", 'w')
        for Note in Servise.dictionary.values():
            f.write(f"{Note.printInFile()}\n")

    def parseLine(line: str):
        atrtributes = line.split(" ; ")
        id = atrtributes[0]
        head = atrtributes[1]
        description = atrtributes[2]
        timeCreate = atrtributes[3]
        timeUpdate = atrtributes[4]
        note = Note(id, head, description)
        note.setTimeCreate(timeCreate)
        note.setTimeUpdate(timeUpdate)
        Servise.dictionary[id] = note

    def load():
        f = open("notebook.csv", 'r')
        while True:
            line = f.readline()
            if not line or len(line) < 1:
                break
            Servise.parseLine(line)
    

        
        
