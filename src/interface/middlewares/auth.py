import logging
from functools import wraps
from http import HTTPStatus
from typing import Callable, Tuple

from src.domain.services.account import decode_access_token
from src.domain.exceptions import InvalidToken


logger = logging.getLogger(__name__)

def Jwt_auth_required(func: Callable) -> Tuple[dict, int]:
    @wraps
    def verify_auth_token(*args, **kwargs)