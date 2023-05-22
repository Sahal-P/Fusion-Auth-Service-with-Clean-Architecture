from rest_framework.routers import Route, SimpleRouter

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from src.infrastructure.factories.account import UserViewSetFactory
from src.interface.routes.account import user_router



class UserRouter(SimpleRouter):
    
    routes = [
        Route(
            url=user_router.get_url('user_login'),
            mapping=user_router.map('user_login'),
            initkwargs={'viewset_factory': UserViewSetFactory},
            name='{basename}-login',
            detail=False
        ),
        Route(
            url=user_router.get_url('user_register'),
            mapping=user_router.map('user_register'),
            initkwargs={'viewset_factory': UserViewSetFactory},
            name='{basename}-register',
            detail=False
        ),
        Route(
            url=user_router.get_url('get_user'),
            mapping=user_router.map('get_user'),
            initkwargs={'viewset_factory': UserViewSetFactory},
            name='{basename}-get_user',
            detail=False
        ),
        Route(
            url=user_router.get_url('refresh_token'),
            mapping=user_router.map('refresh_token'),
            initkwargs={'viewset_factory': UserViewSetFactory},
            name='{basename}-refresh_token',
            detail=False
        ),
        Route(
            url=user_router.get_url('log_out'),
            mapping=user_router.map('log_out'),
            initkwargs={'viewset_factory': UserViewSetFactory},
            name='{basename}-logout',
            detail=False
        ),
    ]
    
class AdminRouter(SimpleRouter):
    
    routes = [
        Route(
            url=user_router.get_url('user_login'),
            mapping=user_router.map('user_login'),
            initkwargs={'viewset_factory': UserViewSetFactory},
            name='{basename}-login',
            detail=False
        ),
        Route(
            url=user_router.get_url('user_register'),
            mapping=user_router.map('user_register'),
            initkwargs={'viewset_factory': UserViewSetFactory},
            name='{basename}-register',
            detail=False
        ),
        Route(
            url=user_router.get_url('get_user'),
            mapping=user_router.map('get_user'),
            initkwargs={'viewset_factory': UserViewSetFactory},
            name='{basename}-get_user',
            detail=False
        ),
        Route(
            url=user_router.get_url('refresh_token'),
            mapping=user_router.map('refresh_token'),
            initkwargs={'viewset_factory': UserViewSetFactory},
            name='{basename}-refresh_token',
            detail=False
        ),
    ]