from datetime import datetime, timezone

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db, login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False,
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
    )

    password_hash = db.Column(
        db.String(256),
        nullable=False,
    )

    xp = db.Column(
        db.Integer,
        default=0,
        nullable=False,
    )

    level = db.Column(
        db.Integer,
        default=1,
        nullable=False,
    )

    completed_modules = db.Column(
        db.Integer,
        default=0,
        nullable=False,
    )

    is_admin = db.Column(
        db.Boolean,
        default=False,
        nullable=False,
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(
            self.password_hash,
            password,
        )


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(
        db.String(50),
        nullable=False,
    )

    question_text = db.Column(
        db.String(500),
        nullable=False,
    )

    option_a = db.Column(
        db.String(300),
        nullable=False,
    )

    option_b = db.Column(
        db.String(300),
        nullable=False,
    )

    option_c = db.Column(
        db.String(300),
        nullable=False,
    )

    option_d = db.Column(
        db.String(300),
        nullable=False,
    )

    correct_option = db.Column(
        db.String(1),
        nullable=False,
    )


class AssessmentResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False,
    )

    category = db.Column(
        db.String(50),
        nullable=False,
    )

    correct_answers = db.Column(
        db.Integer,
        nullable=False,
    )

    total_questions = db.Column(
        db.Integer,
        nullable=False,
    )

    percentage = db.Column(
        db.Float,
        nullable=False,
    )

    date_completed = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )


class ModuleProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False,
    )

    module_name = db.Column(
        db.String(100),
        nullable=False,
    )

    xp_awarded = db.Column(
        db.Integer,
        default=0,
        nullable=False,
    )

    completed = db.Column(
        db.Boolean,
        default=True,
        nullable=False,
    )

    date_completed = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "module_name",
            name="unique_user_module",
        ),
    )

class BehaviourReflection(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False,
    )

    module_name = db.Column(
        db.String(100),
        nullable=False,
    )

    confidence = db.Column(
        db.String(30),
        nullable=False,
    )

    safer_decision = db.Column(
        db.String(30),
        nullable=False,
    )

    key_learning = db.Column(
        db.Text,
        nullable=False,
    )

    date_completed = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
class UserEvaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False,
    )

    learning_clarity = db.Column(db.Integer, nullable=False)
    recommendation_usefulness = db.Column(db.Integer, nullable=False)
    scenario_engagement = db.Column(db.Integer, nullable=False)
    confidence_improvement = db.Column(db.Integer, nullable=False)
    overall_satisfaction = db.Column(db.Integer, nullable=False)

    suggestions = db.Column(db.Text, nullable=True)

    date_completed = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    user = db.relationship(
        "User",
        backref=db.backref(
            "evaluations",
            lazy=True,
        ),
    )
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))