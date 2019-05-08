from flask import Flask, request
from flask_restful import Api, Resource
import json
import os
from models import db, User, Article, Comment, Like

basedir = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
app = Flask(__name__)
app.config.update({
	'SQLALCHEMY_TRACK_MODIFICATIONS' : True,
	'SQLALCHEMY_DATABASE_URI' : SQLALCHEMY_DATABASE_URI,
})

api = Api(app)
db.init_app(app)

def serializer(l):
	ret = ''
	for row in l:
		ret += row.serialize()
	return ret

class UserList(Resource):
	def get_user(self):
		users= User.query.all()
		return users

	def post(self):
		r_
