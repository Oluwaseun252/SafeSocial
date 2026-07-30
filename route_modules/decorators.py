from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def admin_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))

        if not current_user.is_admin:
            flash("You do not have permission to access that page.", "danger")
            return redirect(url_for("dashboard"))

        return function(*args, **kwargs)

    return decorated_function