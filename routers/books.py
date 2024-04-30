from fastapi import APIRouter
from fastapi import HTTPException, Path, Query
from tools import Book, getNewId, books
from schemas.schemas import BookRequest


books_router = APIRouter(
    prefix='/book',
    tags=['books endpoints']
)


# ----------------------------- additional tools -----------------------------
@books_router.get('/')
def get_books():
    return books


@books_router.get('/{book_id}')
def get_book_by_id(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Not found!')


@books_router.post('/')
def add_book(book_body: BookRequest):
    book = Book(getNewId(), book_body.title, book_body.author)
    books.append(book)
    return book


@books_router.put('/{book_id}')
def update_book(book_body: BookRequest, book_id: int = Path(gt=0)):
    for book in books:
        if book.id == book_id:
            book.title = book_body.title
            book.author = book_body.author
            return book
    raise HTTPException(status_code=404, detail='Not found!')


@books_router.delete('/')
def delete_book(book_id: int = Query(gt=0)):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return book
    raise HTTPException(status_code=404, detail='Not found!')