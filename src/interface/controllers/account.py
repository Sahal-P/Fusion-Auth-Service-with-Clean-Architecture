import logging
from http import HTTPStatus
from typing import Tuple
from src.domain.exceptions import EntityDuplicate
from src.domain.services.account import create_access_token, create_refresh_token
from src.interface.serializers.account import UserRegisterSerializer, NewUserSerializer, UserLoginSerializer, TokenSerializer

logger = logging.getLogger(__name__)

class UserController:
    
    def __init__(self, user_interactor):
        self.user_interactor = user_interactor
        
    def login(self, params: dict) -> Tuple[dict, int]:
        
        logger.info('Login user with params: %s', str(params))
        data = UserLoginSerializer().load(params)

        if 'errors' in data:
            logger.error('Error Deserializing params: %s', str(data['errors']))
            return data, HTTPStatus.BAD_REQUEST.value
        try:
            user = self.user_interactor.login(**data)
        except Exception as err:
            logger.error("Error Login user with params: %s", str(params), err.message)
            return {'error': err.message}, HTTPStatus.BAD_REQUEST.value
        
        user = self.user_interactor.update(user.id)
        token = create_access_token(user.id)
        refresh = create_refresh_token(user.id)
        
        logger.info('User succesfully logged in - %s', str(token))
        
        return TokenSerializer().dump(token), TokenSerializer().dump(refresh), HTTPStatus.OK.value

    def register(self, params: dict) -> Tuple[dict, int]:
        
        logger.info('Registering user with params: %s', str(params))
        data = UserRegisterSerializer().load(params)
        if 'errors' in data:
            logger.error('Error deserializing params: %s', str(data['errors']))
            return data, HTTPStatus.BAD_REQUEST.value
        try:
            user = self.user_interactor.register(**data)
        except EntityDuplicate as err:
            # EntityDuplicate
            logger.error('Error creating duplicate user with params %s: %s', str(params), err.message)
            return {'error': err.message}, HTTPStatus.BAD_REQUEST.value
        
        logger.info('User successfully created: %s', str(user))
        return NewUserSerializer().dump(user), HTTPStatus.CREATED.value
    
    def get_user(self, token) -> Tuple[dict, int]:
        return None, None
    