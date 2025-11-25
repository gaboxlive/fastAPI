from common.book_dto import BookRequest
from common.booksconstants import BOOKS
from dao.Book import BookDAO


class BookService:
    def __init__(self):
        pass

    @staticmethod
    def save_book(book_request: BookRequest) -> BookRequest:
        new_book_dao = BookRequest.book_request_to_dao(book_request)
        if new_book_dao.id is None:
            new_book_dao.id = BookService.find_book_next_id()
        BOOKS.append(new_book_dao)
        return new_book_dao.to_dto()

    @staticmethod
    def get_book_by_id(book_id: int) -> BookRequest | None:
        found_book = None
        for book in BOOKS:
            if book.id == book_id:
                found_book = book
        return found_book

    @staticmethod
    def find_book_next_id() -> int:
        return 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    @staticmethod
    def book_request_to_dao(book_request: BookRequest) -> BookDAO:
        return BookDAO(
            id=book_request.bookId,
            title=book_request.bookTitle,
            author=book_request.bookAuthor,
            description=book_request.bookDescription,
            rating=book_request.bookRating
        )

    @staticmethod
    def book_dao_to_dto(book_dao) -> BookRequest:
        return BookRequest(
            bookId=book_dao.id,
            bookTitle=book_dao.title,
            bookAuthor=book_dao.author,
            bookDescription=book_dao.description,
            bookRating=book_dao.rating
        )