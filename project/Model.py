from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

class Note(db.Model):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(4000))
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebook.id'),
        nullable=False)

class Notebook(db.Model):
    __tablename__ = 'notebook'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    notes = db.relationship('Note', backref='notebook', lazy=True)

class NoteSchema(ma.Schema):
    id = fields.Integer()
    title = fields.String(required=True)
    content = fields.String(required=True)
    notebook_id = fields.Integer(required=True)
