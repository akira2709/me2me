from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import db, uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get('/items')
async def return_items():
    return await db.get_items()

@app.get('/login/{token}')
async def return_user(token: str):
    return await db.get_user(token)

@app.get('/auth')
async def return_auth_token():
    return await db.auth()

@app.get('/confirm/{login}/{token}')
async def confirm_user(login: str, token: str):
    return await db.confirm_user(login, token)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)

