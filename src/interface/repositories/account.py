from src.domain.entities.account import UserEntity

class UserRepository:
    
    def __init__(self, db_repo:object) -> None:
        self.db_repo = db_repo
        
    def login(self, email:str, password:str) -> UserEntity:
        return self.db_repo.get(email, password)
    
    def register(self, email: str, password: str, phone: str, username: str, name: str, surname: str ) -> UserEntity:
        return self.db_repo.create(email, password, phone, username, name, surname)
    
    def update(self, user_id: int, token: dict) -> UserEntity:
        return self.db_repo.update(user_id, token)
    
    def refresh_token(self, data: dict):
        return self.db_repo.refresh_token(data)
    
    def logout(self, data: dict):
        return self.db_repo.logout(data)
    
    def get_user(self, user_id: int):
        return self.db_repo.get_user(user_id)