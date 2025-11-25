from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {
        'title': 'Titulo 1',
        'author': 'Gabriel Cruz',
        'category': 'Ciencia',
    },
    {
        'title': 'Titulo 2',
        'author': 'Martha Cruz',
        'category': 'Idiomas',
    },
    {
        'title': 'Titulo 3',
        'author': 'Einstein',
        'category': 'Ciencia',
    },
    {
        'title': 'Titulo 4',
        'author': 'Luis Herandez',
        'category': 'Futbol',
    },
    {
        'title': 'Titulo 5',
        'author': 'Ricardo Salinas',
        'category': 'Economía',
    },
    {
        'title': 'Titulo 6',
        'author': 'Gabriel Cruz',
        'category': 'Matemáticas',
    },
    {
        'title': 'Titulo 7',
        'author': 'Thalia',
        'category': 'Musica',
    }
]

#path parameters: request parameters attached to url.
#dynamic path parameters

#query parameters ?name=value
#a query parameter are attached after a ?, they are key value pairs ?variable=valor

@app.get('/books')
async def get_books():
    return BOOKS

@app.get('/books/mybook')
async def get_books():
    return {
        'book_title': 'my favorite book'
    }

@app.get('/books/{book_title}')
async def get_books(book_title: str):
    book_to_return = {}
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return book_to_return

@app.get('/books/by_author/{author}')
async def get_books_by_author(author: str):
    print('##################sssss')
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/by_author/')
async def get_books_by_author(author: str):
    print('##################')
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/by_category/')
async def read_category_by_query(category: str):
   books_to_return = []
   for book in BOOKS:
       if book.get('category').casefold() == category.casefold():
           books_to_return.append(book)
   return books_to_return


#mixing path and query parameters
@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


#post. used to create data. Para recibir datos, se necesita el metodo Body importado de FastAPI
@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

#PUT. Used to update data. Accept body like post
@app.put('/books/update_book')
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

#DELETE. used to delete data
@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            del BOOKS[i]
            break