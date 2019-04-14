from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

@api.route('/hello', endpoint='world')
class TodoSimple(Resource):
    def get(self):
        return {"milad": "shahali"}
 

if __name__ == '__main__':
    app.run(debug=True)
