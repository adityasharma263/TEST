# -*- coding: utf-8 -*-
__author__ = 'aditya_sharma'
"""base class for every model class"""
from books import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column('id', db.Integer, primary_key=True, index=True)
    created_at = db.Column('created_at', db.DateTime(timezone=True), default=db.func.current_timestamp())
    updated_at = db.Column('updated_at', db.DateTime(timezone=True), default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())

    def save(self):
        db.session.add(self)
        db.session.commit()
        db.session.flush()

    @staticmethod
    def insert(obj):
        db.session.add(obj)
        db.session.commit()
        db.session.flush()

    @staticmethod
    def update_db():
        db.session.commit()
        db.session.flush()

    @classmethod
    def merge(cls, obj):
        db.session.merge(obj)
        db.session.commit()
