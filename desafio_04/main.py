import jwt

ALGORITHIM = 'HS256'

SECRET_WORD = 'acelera'


def create_token(data, secret=SECRET_WORD):
    return jwt.encode(payload=data, key=secret, algorithm=ALGORITHIM)


def verify_signature(token):
    try:
        return jwt.decode(token, key=SECRET_WORD, algorithms=ALGORITHIM)
    except jwt.InvalidTokenError:
        return {'error': 2}
