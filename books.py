from fastapi import FastAPI, APIRouter, Body

from common.book_dto import BookRequest
from service.BookService import BookService

app = FastAPI(
    openapi_url='/api/v1/openapi.json',
    docs_url='/api/v1/docs',
)

router_v1 = APIRouter(prefix='/api/v1/books')

@router_v1.get('/')
async def read_all_books():
    book_service = BookService()
    return {'data': book_service.get_all_books()}

@router_v1.get('/{book_id}')
async def get_book_by_id(book_id: int):
    found_book = BookService().get_book_by_id(book_id)
    return {'data': found_book}

@router_v1.get('/by_rating/')
async def read_books_by_rating(book_rating: int):
    books_by_rating = BookService().get_books_by_rating(book_rating)
    return {'data': books_by_rating}

@router_v1.get('/publish/')
async def read_books_by_published_date(published_date: int):
    return {'data': BookService().get_books_by_published_date(published_date)}

@router_v1.post('/')
async def create_book(book_request: BookRequest):
    book_service = BookService()
    return {'data': book_service.save_book(book_request)}

@router_v1.put('/')
async def update_book(book_request: BookRequest):
    book_service = BookService().update_book(book_request)
    return {'updated_record': book_service}

@router_v1.delete('/')
async def delete_book_by_id(book_id: int):
    return {'deleted_record': BookService().delete_book_by_id(book_id)}
app.include_router(router_v1)
