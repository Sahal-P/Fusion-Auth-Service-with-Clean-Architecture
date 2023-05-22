import logging
from http import HTTPStatus
from typing import Tuple
from src.domain.exceptions import EntityDuplicate
from rest_framework import exceptions
from src.domain.services.account import create_access_token, create_refresh_token
from src.interface.serializers.account import UserRegisterSerializer, NewUserSerializer, UserLoginSerializer, TokenSerializer, RefreshTokenSerializer, UserSerializer
from src.interface.middlewares.auth import Jwt_auth_required 
from colorama import Fore

logger = logging.getLogger(__name__)

class UserController:
    
    def __init__(self, user_interactor):
        self.user_interactor = user_interactor
        
    def login(self, params: dict) -> Tuple[dict, int]:
        
        logger.info(f'{Fore.GREEN}Login user with params: %s', str(params))
        data = UserLoginSerializer().load(params)

        if 'errors' in data:
            logger.error(f'{Fore.RED}Error Deserializing params: %s', str(data['errors']))
            return data, HTTPStatus.BAD_REQUEST.value
        try:
            user = self.user_interactor.login(**data)
        except Exception as err:
            logger.error("Error Login user with params: %s", str(params), err)
            raise exceptions.AuthenticationFailed('User does not exits with this data')
            
        
        token = create_access_token(user.id)
        refresh = TokenSerializer().dump(create_refresh_token(user.id))
        user = self.user_interactor.update(user.id, refresh)
        
        logger.info(f'{Fore.LIGHTGREEN_EX}User succesfully logged in - %s', str(token))
        
        return TokenSerializer().dump(token), refresh, HTTPStatus.OK.value

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
    
    @Jwt_auth_required
    def get_user(self, token: str = None) -> Tuple[dict, int]:
        data = TokenSerializer().load({'token':token})
        if 'errors' in data:
          return data, HTTPStatus.BAD_REQUEST.value
        try:
            user = self.user_interactor.get_user(data['payload'])
        except:
            pass
        return UserSerializer().dump(user), HTTPStatus.OK.value
    
    def refresh_token(self, params) -> Tuple[dict, int]:
        data = RefreshTokenSerializer().load(params)
        if 'errors' in data:
          return data, HTTPStatus.BAD_REQUEST.value
        try:
            token = self.user_interactor.refresh_token(data)
        except EntityDuplicate as err:
            logger.error('Error verifying refresh with params %s: %s', str(params), err.message)
            return {'error': err.message}, HTTPStatus.BAD_REQUEST.value
        new_access = create_access_token(data['payload'])
        logger.info('token successfully created: %s', str(token))
        return TokenSerializer().dump(new_access), HTTPStatus.CREATED.value
    
    def logout(self, params) -> Tuple[dict, int]:
        data = RefreshTokenSerializer().load(params)
        if 'errors' in data:
            return data, HTTPStatus.BAD_REQUEST.value
        try:
            logout = self.user_interactor.logout(data)
        except Exception as err:
            logger.error('Error verifying refresh with params %s: %s', str(params), err)
            return {'error': err}, HTTPStatus.BAD_REQUEST.value
        return logout, HTTPStatus.OK.value