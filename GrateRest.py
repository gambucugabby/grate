#----
#Need flask...or some sort of webserver.  Chosing flask for simplicity - all config
#in code (no one needs dynamic, configurable endpoints, but could do this if needed).
#
#jsonify b/c there's no way I'm going to manually create JSON - my vision is bad enough
#
#flask-restful b/c it let sme setup my API endpoints easily
#
#Post records function - any of the 3 formats
#get - return by gender
#get - retrun by birthdate
#get - return by name`  ``
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
import grate

app = Flask(__name__)
api = Api(app)
class gender(Resource):
    def get(self):
        return {'GenderSort': dumps(grate.ProcFiles('', 1))}

class birthday(Resource):
    def get(self):
        return {'BirthdaySort': dumps(grate.ProcFiles('', 2))}

class empnm(Resource):
    def get(self):
        return {'NameSort': dumps(grate.ProcFiles('', 4))}

class addppl(Resource):
    def post(self):
        lastname=request.json['lastname']
        firstname=request.json['firstname']
        gender=request.json['gender']
        color=request.json['color']
        bdate=request.json['birthday']
        return {'status':'success'}

api.add_resource(gender, '/people/gender')
api.add_resource(birthday, '/people/birthday')
api.add_resource(empnm, '/people/name')
api.add_resource(addppl, '/add')


if __name__ == '__main__':
     app.run(port='1234') #b/c it was good enough for president Skroob's luggage
