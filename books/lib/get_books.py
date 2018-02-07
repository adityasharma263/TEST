# -*- coding: utf-8 -*-
__author__ = 'aditya_sharma'

from books.models.Authors import Author
from books.serialize import AuthorSerialize


def get_books_from_author(author):
    author_data = Author.query.filter_by(name=author).first()
    result = AuthorSerialize().dump(author_data)
    return result.data
