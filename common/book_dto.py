from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class BookRequest(BaseModel):
    #bookId: Optional[int] = None
    bookId: Optional[int] = Field(description="bookId is not needed on create", default = None)
    bookTitle: str = Field(min_length=3)
    bookAuthor: str = Field(min_length=1)
    bookDescription: str = Field(min_length=1, max_length=100)
    bookRating: int = Field(gt=0, lt=6)
    bookPublishedDate: int = Field(gt=1999, lt=2031)

    #display a custom example on endpoint that use this model
    model_config = {
        'json_schema_extra': {
            'example': {
                'bookId': 'Book ID',
                'bookTitle': 'Book Title',
                'bookAuthor': 'Author',
                'bookDescription': 'Book Description',
                'bookRating': 5,
                'bookPublishedDate': 2029
            }
        }
    }