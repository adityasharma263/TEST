from books import ma
from books.models.Authors import Author
from books.models.Books import Book


class BookSerialize(ma.ModelSchema):

    class Meta:
        model = Book
        exclude = ('created_at', 'updated_at', 'id', 'book')


class AuthorSerialize(ma.ModelSchema):
    books = ma.Nested('BookSerialize', many=True)

    class Meta:
        model = Author
        exclude = ('created_at', 'updated_at', 'id', 'name')

