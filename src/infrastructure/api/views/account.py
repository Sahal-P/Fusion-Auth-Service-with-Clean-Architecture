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
        response.set_cookie(key="Access_token", value=payload['token'], httponly=True)
        response.set_cookie(key="Refresh_token", value=refresh['token'], httponly=True)
        return response
    
    def get_user(self, request: Request, *args, **kwargs) -> Response:
        token = request.headers.get('Authorization', '')
        payload, status = self.controller.get_user(token=token)
        return Response(data=payload, status=status)
    
    def register(self, request: Request, *args, **kwargs) -> Response:
        data = request.data        
        payload, status = self.controller.register(data)
        print(self.controller)
        return Response(data=payload, status=status)