import jwt
from datetime import timedelta, datetime
from passlib.context import CryptContext
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

#настройки для хеширования пароля
security = HTTPBearer()
pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

#функция получения хеша из пароля
def get_password_hash(password):
    return pwd_context.hash(password)

#сверка пароля и хеша
def verify_password(input_pass, hash_pass):
    return pwd_context.verify(input_pass, hash_pass)

# Секретный ключ, на его основе генерируется JWT токен
secret = 'Подписывайтесь на постал аск'

# создание JWT токена с временем жизни 30 минут
def encode_token(username):
    payload = {
        'exp': datetime.utcnow() + timedelta(minutes=30),
        'iat': datetime.utcnow(),
        'sub': username
    }
    return jwt.encode(
        payload,
        secret,
        algorithm='HS256'
    )

# декодирование JWT токена
def decode_token(token):
    try:
        payload = jwt.decode(
            token,
            secret,
            algorithms=['HS256']
        )
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, 'Просрочено')
    except jwt.InvalidTokenError as e:
        raise HTTPException(401, 'Плохой токен')

# мидлваре для защиты маршрутов
def auth_wrapper(auth: HTTPAuthorizationCredentials = Security(security)):
    return decode_token(auth.credentials)