class Note:
    def __init__(self, id_note=None, athour=None, description=None, content=None, status=None,createdAt=None, updatedAt=None) -> None:
        self.id_note = id_note
        self.status=status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.athour = athour
        self.description = description
        self.content = content
    ## getter and setter
    def getStatus(self):
        return self.status
    def getIdNote(self):
        return self.id_note

    def getAthour(self):
        return self.athour

    def getDescription(self):
        return self.description

    def getContent(self):
        return self.content

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def setNewDescription(self, desc):
        self.description = desc

    def setNewContent(self, content):
        self.content = content

    def setNewUpdatedAt(self, newDate):
        self.updatedAt = newDate


class User:
    def __init__(self, username=None, notes=[], createdAt=None, updatedAt=None, *args, **kwargs) -> None:
        self.username = username
        self.notes = notes
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def getUsername(self):
        return self.username

    def getNotes(self):
        return self.notes
