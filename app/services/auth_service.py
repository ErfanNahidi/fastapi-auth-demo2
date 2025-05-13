from passlib.context import CryptContext
from app.db.db import database, users, roles
from app.schemas.user import UserCreate
from app.core.security import create_access_token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    async def register(self, user: UserCreate):
        hashed = pwd_context.hash(user.password)
        query = users.insert().values(email=user.email, hashed_password=hashed, role_id=2)
        user_id = await database.execute(query)
        return {"id": user_id, "email": user.email, "is_active": True, "role": "user"}

    async def authenticate_user(self, email: str, password: str):
        query = users.select().where(users.c.email == email)
        db_user = await database.fetch_one(query)
        if not db_user or not pwd_context.verify(password, db_user["hashed_password"]):
            return None
        token = create_access_token({"sub": db_user["id"]})
        return {"access_token": token, "token_type": "bearer"}