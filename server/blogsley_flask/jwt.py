import jwt
import json
import datetime
from loguru import logger

from __blogsley__ import app
from blogsley_flask.user import User

def encode_auth_token(**kwargs):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30, seconds=0),
        'iat': datetime.datetime.utcnow()
    }

    for key, value in kwargs.items():
        payload[key] = value

    return jwt.encode(
        payload,
        app.config.get('SECRET_KEY')
    )

def load_user(info):
    token = decode_auth_token(info.context)
    logger.debug(f"token: {token}")
    return User.query.get(token['id'])

def decode_auth_token(request):
    auth_token = request.headers.get('Authorization')
    if not auth_token or auth_token == 'null':
        return None
    logger.debug(f"auth_token: {auth_token}")
    secret = app.config.get('SECRET_KEY')
    logger.debug(f"secret: {secret}")
    if not auth_token:
        auth_token = ''
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        #payload = json.loads(payloads)
        return payload
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
