from src.interface.controllers.account import UserController
from src.interface.routes.core.constants import HTTP_VERB_GET, HTTP_VERB_POST
from src.interface.routes.core.routing import Route, Router

user_router = Router()
user_router.register(
    [
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"^account/users/login/$",
            controller=UserController,
            method="login",
            name="user_login",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"^account/users/register/$",
            controller=UserController,
            method="register",
            name="user_register",
        ),
        Route(
            http_verb=HTTP_VERB_GET,
            path=r"^account/users/$",
            controller=UserController,
            method="get_user",
            name="get_user",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"^account/users/token/refresh/$",
            controller=UserController,
            method="refresh_token",
            name="refresh_token",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"^account/users/logout/$",
            controller=UserController,
            method="logout",
            name="log_out",
        ),
    ]
)
