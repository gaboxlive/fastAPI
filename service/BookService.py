from common.book_dto import BookRequest
from common.booksconstants import BOOKS
from dao.Book import BookDAO


class BookService:
    def __init__(self):
        pass

    @staticmethod
    def get_all_books() -> list[BookRequest]:
        books_to_return = []
        for book in BOOKS:
            books_to_return.append(BookService.book_dao_to_dto(book))
        return books_to_return

    @staticmethod
    def save_book(book_request: BookRequest) -> BookRequest:
        new_book_dao = BookService.book_request_to_dao(book_request)
        if new_book_dao.id is None:
            new_book_dao.id = BookService.find_book_next_id()
        BOOKS.append(new_book_dao)
        print(new_book_dao.id)
        return BookService.book_dao_to_dto(new_book_dao)

    @staticmethod
    def get_book_by_id(book_id: int) -> BookRequest | None:
        found_book = None | BookDAO
        for book in BOOKS:
            if book.id == book_id:
                found_book = book
        return BookService.book_dao_to_dto(found_book)

    @staticmethod
    def get_books_by_rating(book_rating: int) -> list[BookRequest]:
        books_to_return = []
        for book in BOOKS:
            if book.rating == book_rating:
                books_to_return.append(book)
        return books_to_return

    @staticmethod
    def get_books_by_published_date(published_date: int) -> list[BookRequest]:
        books_to_return = []
        for book in BOOKS:
            if book.published_date == published_date:
                books_to_return.append(BookService.book_dao_to_dto(book))
        return books_to_return

    @staticmethod
    def update_book(book_request: BookRequest) -> bool:
        updated = False
        for i in range(len(BOOKS)):
            if BOOKS[i].id == book_request.bookId:
                BOOKS[i] = BookService.book_request_to_dao(book_request)
                updated = True
        return updated

    @staticmethod
    def delete_book_by_id(book_id: int) -> bool:
        deleted = False
        for i in range(len(BOOKS)):
            if BOOKS[i].id == book_id:
                BOOKS.pop(i)
                deleted = True
                break
        return deleted


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
            rating=book_request.bookRating,
            published_date=book_request.bookPublishedDate
        )

    @staticmethod
    def book_dao_to_dto(book_dao) -> BookRequest:
        return BookRequest(
            bookId=book_dao.id,
            bookTitle=book_dao.title,
            bookAuthor=book_dao.author,
            bookDescription=book_dao.description,
            bookRating=book_dao.rating,
            bookPublishedDate=book_dao.published_date
        )