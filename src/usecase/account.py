

class UserInteractor:
    
    def __init__(self, user_repo: object) -> None:
        self.user_repo = user_repo
    
    def login(self, email: str, password: str) -> None:
        return self.user_repo.login(email, password)
    
    def register(self, email: str, password: str, phone: str, username: str, name: str, surname: str = None ) -> None:
        return self.user_repo.register( email, password, phone, username, name, surname )
    
    def update(self, user_id: str) -> None:
        return self.user_repo.update(user_id)