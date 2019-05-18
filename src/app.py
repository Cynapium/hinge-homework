from flask import Flask
from flask_restful import Api
from database import initializeDatabase
from user import User
from users import Users
from likes import Likes, Rating

app = Flask(__name__)
api = Api(app)

###############################################################################
###############################################################################

initializeDatabase("hinge.db", "schema_database.json")

api.add_resource(Users, "/<string:version>/users/")
api.add_resource(User, "/<string:version>/users/<int:user_id>")
api.add_resource(Likes, "/<string:version>/users/<int:user_id>/likes")
api.add_resource(Rating, "/<string:version>/users/<int:user_id>/<string:rating>/<int:user_target>")
app.run(debug=True)
