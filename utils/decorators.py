from functools import wraps
from flask import session, redirect, url_for, current_app


def public_route(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Skip login check for this route
        return f(*args, **kwargs)
    # Mark this route as public
    decorated_function.is_public = True
    return decorated_function
