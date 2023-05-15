from django.db.utils import IntegrityError
from django.utils import timezone

from src.domain.entities.account import UserEntity
from src.infrastructure.orm.db.account.models import User
from src.domain.exceptions import EntityDuplicate, EntityDoesNotExist

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
        return user.map(fields=['id', 'username', 'email', 'is_active', 'last_login'])
    
    def update(self, user_id: int) -> UserEntity:
        user = User.objects.get(pk=user_id)
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        return user.map(fields=['id', 'username', 'email', 'is_active', 'last_login'])
