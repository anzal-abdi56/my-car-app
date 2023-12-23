from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import Car,User,db

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["JSONIFY_PRETTYPRINT_REGULAR"]=True
migrate = Migrate(app,db)
db.init_app(app)


if __name__ =="__main__":
    app.run(port=5000,debug=True)