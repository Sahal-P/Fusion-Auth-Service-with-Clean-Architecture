from dataclasses import dataclass

@dataclass
class UserEntity:
    id: int = None
    name: str = None
    surname: str = None
    username: str = None
    email: str = None
    password: str = None
    is_active: bool = False
    last_login: str = None
    date_joined: str = None
    
    def __post_init__(self):
        pass

@dataclass
class TokenEntity:
    token: str = None
    
    def __str__(self) -> str:
        return f'Token: {self.token}'

    @staticmethod
    def to_string(token: 'TokenEntity') -> str:
        return str(token)
