from flask import Flask
from flask_restful import Api
from db.database import initializeDatabase
from users import Users, User
from ratings import Likes, Matches, Recommendations, Rating

app = Flask(__name__)
api = Api(app)

initializeDatabase("src/db/hinge-homework-barbara.db", "src/db/schema_database.json")

api.add_resource(Users, "/<string:version>/users")
api.add_resource(User, "/<string:version>/users/<int:user_id>")
api.add_resource(Likes, "/<string:version>/users/<int:user_id>/likes")
api.add_resource(Matches, "/<string:version>/users/<int:user_id>/matches")
api.add_resource(Recommendations, "/<string:version>/users/<int:user_id>/recommendations")
api.add_resource(Rating, "/<string:version>/users/<int:user_id>/<string:rating>/<int:user_target>")
app.run(debug=True)
