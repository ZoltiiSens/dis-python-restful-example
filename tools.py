books = []


def getNewId():
    maxId = 0
    for book in books:
        maxId = max(book.id, maxId)
    return maxId + 1


class Book:
    id: int
    title: str
    author: str

    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author


books.append(Book(1, 'qqq', 'Ivan'))
books.append(Book(2, 'wwww', 'Daniil'))