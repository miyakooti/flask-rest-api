from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}


class SignupResource(Resource):
    def post(self):
        # リクエストデータの取得
        data = request.get_json()
        user_id = data.get("user_id")
        password = data.get("password")
        
        # アカウントの作成処理（仮実装）

        if (len(user_id) < 6 or len(user_id) > 20) or (len(password) < 8 or len(password) > 20):
            response_data = {
            "message": "Account creation failed",
            "cause": "required user_id and password"
            }
            status = 400
        else:
            response_data = {
            "message": "Account successfully created",
            "user": {
                "user_id": user_id,
                "nickname": user_id
                    }  
            }
            status = 200


        return response_data, status

api.add_resource(HelloWorld, '/')
api.add_resource(SignupResource, '/signup')


if __name__ == '__main__':
    app.run(debug=True)
