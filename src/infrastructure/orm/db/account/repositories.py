from django.db.utils import IntegrityError
from django.utils import timezone
import datetime
from src.domain.entities.account import UserEntity, TokenEntity
from src.infrastructure.orm.db.account.models import User, UserToken
from rest_framework import exceptions
from src.domain.exceptions import EntityDuplicate, EntityDoesNotExist, InvalidToken

class UserDataBaseRepository:
    
    def create(self, email: str, password: str, phone: str, username: str, name: str, surname: str = None ) -> UserEntity:
        try:
            user = User.objects.create(email=email, password=password,
                                       phone=phone, username=username, 
                                       name=name, surname=surname  
                                    )
        except IntegrityError:
            raise EntityDuplicate(message="Already exitst a user with this data.")
        # except Exception as e:
        #     raise e
        return user.map(fields=['id', 'email'])
    
    def get(self, email: str, password: str) -> UserEntity:
        try:
            user = User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            raise EntityDoesNotExist(message='User does not exits with this data')
            # raise exceptions.NotAuthenticated('User does not exits with this data')
        return user.map(fields=['id', 'username', 'email', 'is_active', 'last_login'])
    
    def update(self, user_id: int, data: dict) -> UserEntity:
        user = User.objects.get(pk=user_id)
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        user_token = UserToken.objects.create(
            user_id=user.id,
            token=data['token'],
            expired_at= datetime.datetime.utcnow() + datetime.timedelta(days=7),
            
        )
        return user.map(fields=['id', 'username', 'email', 'is_active', 'last_login'])

    def refresh_token(self, data: dict) -> TokenEntity:
        try:
            verify_token = UserToken.objects.filter( user_id= data['payload'], token = data['token'], expired_at__gt = datetime.datetime.now(tz=datetime.timezone.utc)).exists()
        except:
            exceptions.AuthenticationFailed('Token verification failed')
        if not verify_token:
            raise exceptions.NotAuthenticated("Token verification failed")
        return data
    
    def logout(self, data: dict):
        try:
            UserToken.objects.filter(token=data['token']).delete()
        except:
            raise exceptions.ParseError()
        return data['token']
    
    def get_user(self, user_id: int) -> UserEntity:
        user = User.objects.filter(pk=user_id).first()
        test = user.map(fields=['id', 'username', 'email', 'is_active', 'last_login'])
        print(test,'llllll')
        return user.map(fields=['id', 'username', 'name', 'email', 'is_active', 'last_login'])
        
        
    # raise InvalidToken(message="Inavlid Token")4