import requests


class RequestHandler:
    base_url:str
    token:str
    email: str
    pwd: str
    def __init__(self, email:str, pwd: str) -> None:
        self.email = email
        self.pwd = pwd
    
    
    def auth(self) -> None: 
        requests.post(f'{self.base_url}', json={
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": self.email,
                    "domain": {
                        "name": "Default"
                    },
                    "password": self.pwd
                }
            }
        }
                          }

                      })

    def get_images(self):
        pass
