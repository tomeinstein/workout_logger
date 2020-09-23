from flask import Flask
from flask_restful import Api

from api.resources.user import User, Users
from api.resources.db_management import close_db

app = Flask(__name__)

api = Api(app)

app.teardown_appcontext(close_db)

api.add_resource(User, '/user', '/user/<int:id>')
api.add_resource(Users, '/users')


app.run()
