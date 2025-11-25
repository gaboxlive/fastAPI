from fastapi import FastAPI, APIRouter, Body

from common.book_dto import BookRequest
from common.booksconstants import BOOKS
from service.BookService import BookService

app = FastAPI(
    openapi_url='/api/v1/openapi.json',
    docs_url='/api/v1/docs',
)

router_v1 = APIRouter(prefix='/api/v1/books')

@router_v1.get('/')
async def read_all_books():
     return BOOKS

@router_v1.post('/')
async def create_book(book_request: BookRequest):
    book_service = BookService()
    return {'data': book_service.save_book(book_request)}

@router_v1.get('/{book_id}')
async def get_book_by_id(book_id: int):
    found_book = BookService().get_book_by_id(book_id)
    return {'data': found_book}


app.include_router(router_v1)
