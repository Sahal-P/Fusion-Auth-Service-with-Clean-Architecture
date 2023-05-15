from src.usecase.account import UserInteractor
from src.infrastructure.orm.db.account.repositories import UserDataBaseRepository
from src.interface.controllers.account import UserController
from src.interface.repositories.account import UserRepository
from src.usecase.account import UserInteractor

class UserDataBaseRepositoryFactory:
    
    @staticmethod
    def get() -> UserDataBaseRepository:
        return UserDataBaseRepository()

class UserRepositoryFactory:
    
    @staticmethod
    def get() -> UserRepository:
        db_repo = UserDataBaseRepositoryFactory.get()
        return UserRepository(db_repo)

class UserInteractorFactory:
    
    @staticmethod
    def get() -> UserInteractor:
        user_repo = UserRepositoryFactory.get()
        return UserInteractor(user_repo)
    
class UserViewSetFactory:
    
    @staticmethod
    def create() -> UserController:
        user_interactor = UserInteractorFactory.get()
        return UserController(user_interactor)