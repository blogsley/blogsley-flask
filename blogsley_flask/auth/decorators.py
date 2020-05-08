from functools import wraps

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        token = kwargs.pop(current_app.config["JWT_TOKEN_ARGUMENT_NAME"])
        try:
            verify_jwt_in_argument(token)
        except Exception as e:
            return AuthInfoField(message=str(e))

        return fn(*args, **kwargs)

    return wrapper