from flask import Flask

from extensions import db, login_manager, migrate
from routes import register_routes


app = Flask(__name__)

app.config["SECRET_KEY"] = "development-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///safesocial.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)

login_manager.login_view = "login"
login_manager.login_message = "Please log in to access that page."
login_manager.login_message_category = "error"


register_routes(app)

# Load the database models before creating the tables.
import models

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)