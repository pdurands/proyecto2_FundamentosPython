
import hashlib

def hash_pwd(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()