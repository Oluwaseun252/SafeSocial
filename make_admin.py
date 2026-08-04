from app import app
from extensions import db
from models import User


EMAIL = "c5030858@shallam.shu.ac.uk"


with app.app_context():
    user = User.query.filter_by(email=EMAIL).first()

    if user is None:
        print(f"No user found with email: {EMAIL}")

    else:
        user.is_admin = True
        db.session.commit()

        print(f"{user.email} is now an administrator.")