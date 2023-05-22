

class UserInteractor:
    
    def __init__(self, user_repo: object) -> None:
        self.user_repo = user_repo
    
    def login(self, email: str, password: str) -> None:
        return self.user_repo.login(email, password)
    
    def register(self, email: str, password: str, phone: str, username: str, name: str, surname: str = None ) -> None:
        return self.user_repo.register( email, password, phone, username, name, surname )
    
    def update(self, user_id: str, token:dict) -> None:
        return self.user_repo.update(user_id, token)
    
    def refresh_token(self, data:dict) -> None:
        return self.user_repo.refresh_token(data)
    
    def logout(self, data:dict) -> None:
        return self.user_repo.logout(data)
    
    def get_user(self, user_id: int):
        return self.user_repo.get_user(user_id)