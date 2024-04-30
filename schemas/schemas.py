from pydantic import BaseModel, Field, field_validator


class BookRequest(BaseModel):
    title: str = Field(min_length=5)
    author: str = Field(max_length=150)

    @field_validator('author')
    def validate_author_field(cls, author_value):
        if author_value.startswith(('_', '%', '@', '#', '№', '!', '?', '&')):
            raise ValueError('Author name should starts with letter or number')
        return author_value
