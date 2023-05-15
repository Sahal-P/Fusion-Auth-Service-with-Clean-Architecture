from src.domain.entities.account import UserEntity

class UserRepository:
    
    def __init__(self, db_repo:object) -> None:
        self.db_repo = db_repo
        
    def login(self, email:str, password:str) -> UserEntity:
        return self.db_repo.get(email, password)
    
    def register(self, email: str, password: str, phone: str, username: str, name: str, surname: str ) -> UserEntity:
        return self.db_repo.create(email, password, phone, username, name, surname)
    
    def update(self, user_id: int) -> UserEntity:
        return self.db_repo.update(user_id)