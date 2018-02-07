# -*- coding: utf-8 -*-
from books import db
from books.models.base import Base


class Book(Base):
    __tablename__ = 'book'
    title = db.Column(db.String, nullable=False)
    publish_date = db.Column(db.DateTime(timezone=True), nullable=True)
    description = db.Column(db.TEXT, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<title %r>' % self.title
