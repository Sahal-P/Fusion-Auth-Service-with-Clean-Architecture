from rest_framework import exceptions
import jwt
import datetime
import hashlib
from src.domain.services.constants import JWT_ALGORITHM, JWT_ACCESS_EXP_DELTA_SECONDS, JWT_REFRESH_DAYS, JWT_KEY, JWT_REFRESH_KEY
from src.domain.entities.account import TokenEntity

def create_access_token(id):
    secret = JWT_KEY
    token = jwt.encode({
        'user_id':id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_ACCESS_EXP_DELTA_SECONDS),
        'iat': datetime.datetime.utcnow()
        }, secret, algorithm = JWT_ALGORITHM)
    return TokenEntity(token)

def decode_access_token(token):
	secret = JWT_KEY
	try:
		payload = jwt.decode(token, secret, algorithms=JWT_ALGORITHM)
		return payload['user_id']
	except Exception as e:
		print(e)
		raise exceptions.AuthenticationFailed('unauthenticated')

def decode_refresh_token(token):
	secret = JWT_REFRESH_KEY
	try:
		payload = jwt.decode(token, secret, algorithms=JWT_ALGORITHM)
		return payload['user_id']
	except Exception as e:
		print(e)
		raise exceptions.AuthenticationFailed('unauthenticated')


def create_refresh_token(id):
    secret = JWT_REFRESH_KEY
    refresh = jwt.encode({
        'user_id':id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=JWT_REFRESH_DAYS),
        'iat': datetime.datetime.utcnow()
        }, secret, algorithm =JWT_ALGORITHM)
    return TokenEntity(refresh)

def generate_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
