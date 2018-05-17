#----
#Need flask...or some sort of webserver.  Chosing flask for simplicity - all config
#in code (no one needs dynamic, configurable endpoints, but could do this if needed).
#
#jsonify b/c there's no way I'm going to manually create JSON - my vision is bad enough
#
#flask-restful b/c it let sme setup my API endpoints easily
#
#Am I cheating?  Arguable.  But no one would write their own web server, JSON-ifier,
#etc if they were doing this real world.  Good, fast work can be achieved by building
#on the work of others.  Touchy-feely viewpoint: "We are who we are because we stand on the shoulders
#of who we were."  Steve Jobs Version (via Picasso): "Good artists copy.  Great artists steal."
#I am neither an artist of a theif.  For the purpsoes of this, I'm a programmer
#which lies somewhere intbetween.  Ok...I'll stop as this has now become an example of what
#comments in code should not be.

#Post records function - any of the 3 formats
#get - return by gender
#get - retrun by birthdate
#get - return by name`  ``
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

class gender(Resource):
    def get(self):
        return {'GenderSort': []}

class birthday(Resource):
    def get(self):
        return {'BirthdaySort': []}

class empnm(Resource):
    def get(self):
        return {'NameSort': []}

class addppl(Resource):
    def post(self):
        lastname=request.json['lastname']
        firstname=request.json['firstname']
        gender=request.json['gender']
        color=request.json['color']
        bdate=request.json['birthday']


api.add_resource(gender, '/people/gender')
api.add_resource(birthday, '/people/birthday')
api.add_resource(empnm, '/people/name')
api.add_resource(addppl, '/add')


if __name__ == '__main__':
     app.run(port='1234') #b/c it was good enough for president Skroob's luggage
