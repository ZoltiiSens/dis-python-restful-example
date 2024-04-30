from fastapi import FastAPI
from routers.books import books_router

app = FastAPI()
app.include_router(books_router)


@app.get('/')
def root():
    return {'hello': 'world!'}



