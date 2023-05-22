from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.interface.controllers.account import UserController

class UserViewSet(ViewSet):
    
    viewset_factory = None
    
    @property
    def controller(self) -> UserController:
        return self.viewset_factory.create()
    
    def login(self, request: Request, *args, **kwargs) -> Response:        
        data = request.data
        payload, refresh, status = self.controller.login(data)
            
        response = Response(data=payload, status=status)
        response.set_cookie(key="Access_token", value=payload['token'], secure=True, httponly=True)
        response.set_cookie(key="Refresh_token", value=refresh['token'], secure=True, httponly=True)
        print(response.headers)
        return response
    
    def get_user(self, request: Request, *args, **kwargs) -> Response:
        token =  request.COOKIES.get('Access_token')
        # token = request.headers.get('Authorization', '')
        payload, status = self.controller.get_user(token = token)
        
        return Response(data=payload, status=status)
    
    def register(self, request: Request, *args, **kwargs) -> Response:
        data = request.data        
        print(data)
        payload, status = self.controller.register(data)
        return Response(data=payload, status=status)
    
    def refresh_token(self, request: Request, *args, **kwargs) -> Response:
        data = {'token': request.COOKIES.get('Refresh_token')}
        payload, status = self.controller.refresh_token(data)
        response = Response(data=payload, status=status)
        if status == 201:
            response.set_cookie(key="Access_token", value=payload['token'], httponly=True)
        return response
    
    def logout(self, request: Request, *args, **kwargs) -> Response:
        data = {'token': request.COOKIES.get('Refresh_token')}
        payload, status = self.controller.logout(data)
        response = Response(data=payload, status=status)
        response.delete_cookie(key="Access_token")
        response.delete_cookie(key="Refresh_token")
        return response
    
# from rest_framework.exceptions import APIException

# class NotFoundAPIException(APIException):
#     status_code = 404
#     default_detail = 'Page not found.'
#     default_code = 'not_found'

# raise NotFoundAPIException()