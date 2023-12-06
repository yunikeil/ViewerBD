from typing import List

from passlib.context import CryptContext
from fastapi import HTTPException, Request


class IpCheck():
    def __init__(self, **kwargs) -> None:
        self.allowed_ips: List[str] = kwargs.get("allowed_ips")
    
    def is_ip_allowed(self, request: Request):
        client_ip = request.client.host
        if not self.allowed_ips or len(self.allowed_ips) == 0:
            return True
        
        if client_ip not in self.allowed_ips:
            raise HTTPException(status_code=403, detail="IP address is not allowed")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Медленная функция хеширования, для защиты от атак по времени


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str, salt: str = None) -> str:
    if salt:  # Не имеет особого смысла, соль автоматически генерируется
        password = password + salt
    return pwd_context.hash(password)
