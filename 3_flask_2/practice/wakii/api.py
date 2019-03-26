from flask import Flask, request
from flask_restful import Api, Resource
import json
import os

app = Flask(__name__)
api = Api(app)

class UserList(Resource) :
	def get(self):
		return 'get method'

	def post(self):
		r_json = request.get_json()
		email = r_json['email']
		password = r_json['password']
		r = []
		if os.path.exists('users.json'):
			with open('users.json', 'r') as fp :
				r = json.loads(fp.read())
		for d in r:
			if email == d['email']:
				return '{} is already exists'.format(email)
		r.append(r_json)
		with open('users.json', 'w') as fp:
			fp.write(json.dumps(r))
		return 'email: {}, pw: {}'.format(email,password)
	

# user.json이라는 문서가 있다면 users.json 텍스트들을 json 타입으로 바꿔 리스트 r 에 저장
# r을for 문으로 뒤져서 입력된 이메일 값이 있는지 비교하고 있다면, 함수 밖으로 나감. 
# 없다면 r 에 추가
# 마지막에 r 전체를 문서에 옮겨 씀.

	def put(self):
		return 'put method'

	def delete(self):
		return 'delete method'

api.add_resource(UserList, '/api/users')

if __name__== '__main__':
	app.run(host='0.0.0.0', port=5012, debug=True)



