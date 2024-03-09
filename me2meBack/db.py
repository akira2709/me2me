import asyncio
import random
import string

import asyncpg
import json
from datetime import datetime, timedelta
import jwt
from nacl import hash

SECRET_KEY = 'me2meSuperSecretKeyThatNobodyKnow'


async def create_token():
    key = str(hash.sha256(''.join(random.choices(string.ascii_letters + string.digits, k=10)).encode()))
    data = {
        'username': str(hash.sha256(''.join(random.choices(string.ascii_letters + string.digits, k=10)).encode())),
        'exp': datetime.utcnow()
    }
    jwt_token = jwt.encode(data, key, algorithm='HS512')[64:128]
    return jwt_token

async def get_items():
    conn = await asyncpg.connect(user='postgres', password='postgres', database='me2me', host='127.0.0.1', port='5432')
    items = await conn.fetch('SELECT * FROM items')
    return items

async def get_user(token):
    conn = await asyncpg.connect(user='postgres', password='postgres', database='me2me', host='127.0.0.1', port='5432')
    user = await conn.fetch('SELECT * FROM users WHERE token = $1', token)
    if not user:
        return None
    if user[0]['expire'] < datetime.utcnow():
        return None
    expire = datetime.utcnow() + timedelta(minutes=180)
    await conn.fetch('UPDATE users SET expire = $1 WHERE token = $2', expire, token)
    return user


async def auth():
    conn = await asyncpg.connect(user='postgres', password='postgres', database='me2me', host='127.0.0.1', port='5432')
    login = SECRET_KEY
    token = await create_token()
    expire = datetime.utcnow() + timedelta(minutes=180)
    rating = 0
    buy = []
    amount = 0
    await conn.fetch('INSERT INTO users (login, token, expire, rating, buy, amount) values ($1, $2, $3, $4, $5, $6)', login, token, expire, rating, buy, amount)
    return token


async def confirm_user(login, token):
    conn = await asyncpg.connect(user='postgres', password='postgres', database='me2me', host='127.0.0.1', port='5432')
    user = await conn.fetch('SELECT * FROM users WHERE login = $1', login)
    new_user = await conn.fetch('SELECT * FROM users WHERE token = $1', token)
    if user:
        await conn.fetch('DELETE FROM users WHERE token = $1', token)
        await conn.fetch('UPDATE users SET token = $1 WHERE login = $2', token, login)
        expire = datetime.utcnow() + timedelta(minutes=180)
        await conn.fetch('UPDATE users SET expire = $1 WHERE login = $2', expire, login)
        return 'user confirmed'
    if not user and new_user:
        await conn.fetch('UPDATE users SET login = $1 WHERE token = $2', login, token)
        expire = datetime.utcnow() + timedelta(minutes=180)
        await conn.fetch('UPDATE users SET expire = $1 WHERE token = $2', expire, token)
        return 'new user added'
    else:
        return 'user does not exist'

