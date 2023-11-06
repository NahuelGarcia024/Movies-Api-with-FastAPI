from jwt import encode

def create_token(data: dict):
   token: str = encode(payLoad=data, key="secret", algorithm="HS256")
   return token