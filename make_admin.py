from app import app
from extensions import db
from models import User


USERNAME = "Admin"


with app.app_context():
    user = User.query.filter_by(username=USERNAME).first()

    if user is None:
        print(f"No user found with username: {USERNAME}")

        print("Available users:")

        for existing_user in User.query.all():
            print(
                existing_user.id,
                existing_user.username,
                existing_user.email,
                existing_user.is_admin,
            )

    else:
        user.is_admin = True
        db.session.commit()

        print(
            f"{user.username} ({user.email}) "
            "is now an administrator."
        )