import logging
from functools import wraps
from http import HTTPStatus
from typing import Callable, Tuple

from src.domain.services.account import decode_access_token
from src.domain.exceptions import InvalidToken
from rest_framework import exceptions

logger = logging.getLogger(__name__)

def Jwt_auth_required(func: Callable) -> Tuple[dict, int]:
    @wraps(func)
    def verify_auth_token(*args, **kwargs) -> Tuple[dict, int]:
        token = kwargs.get('token')
        if not token:
            raise exceptions.NotAuthenticated('unauthenticated')
        try:
            # token = token.split()
            # print(len(token))
            # if len(token) == 2:
            decode_access_token(token)
            # raise exceptions.AuthenticationFailed('unauthenticated')
        except InvalidToken as e:
            logger.exception('Invalid Token')
            return {'error': f'{e.message}: {token}'}, HTTPStatus.UNAUTHORIZED.value
        return func(*args, **kwargs)
    return verify_auth_token