from flask import Flask
from flask_restful import Api
from database import initializeDatabase
from user import User
from users import Users

app = Flask(__name__)
api = Api(app)

###############################################################################
###############################################################################

initializeDatabase()

api.add_resource(User, "/user/<int:user_id>")
api.add_resource(Users, "/users/")
app.run(debug=True)

