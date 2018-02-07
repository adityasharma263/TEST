# -*- coding: utf-8 -*-
from books import db
from books.models.base import Base

association_table = db.Table('association',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)


class Author(Base):
    __tablename__ = 'author'
    name = db.Column(db.String, nullable=False)
    books = db.relationship("Book", secondary=association_table, backref="book")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<name %r>' % self.name