from flask import request
from flask_restful import Resource
from Model import db, Notebook, NotebookSchema

notebooks_schema = NotebookSchema(many=True)
notebook_schema = NotebookSchema()
class NotebookResource(Resource):
    def get(self):
        notebooks = Notebook.query.all()
        print('bla bla')
        print(notebooks)
        notebooks = notebooks_schema.dump(notebooks).data
        return {'status': 'success', 'data': notebooks}, 200
    
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = notebook_schema.load(json_data)
        if errors:
            return errors, 422
        notebook = Notebook.query.filter_by(title=data['title']).first()
        if notebook:
            return {'message': 'notebook already exists'}, 400
        notebook = Notebook(
            title=json_data['title']
            )

        db.session.add(category)
        db.session.commit()

        result = notebook.dump(notebook).data

        return { "status": 'success', 'data': result }, 201