import hashlib

def hash_password(pswd):
    return hashlib.sha256(pswd.encode()).hexdigest()