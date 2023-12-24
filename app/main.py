from fastapi import FastAPI, HTTPException
from services.users.router_admin import router as users_router_admin
from services.users.router_me import router as users_router_me
from databases import Database
from database import db


app = FastAPI(title="My FastAPI Project")

# Подключаем роутеры от различных сервисов
app.include_router(users_router_admin, prefix="/users", tags=["Users Administration"])
app.include_router(users_router_me, prefix="/users/me", tags=["Users"])
# Добавьте другие роутеры здесь

@app.get("/")
async def root():
    query = '''
        INSERT INTO users 
        SET 
            email              = :email,
            password           = :password,
            name               = :name, 
            last_language      = :language,

            is_email_verified  = 0,
            is_active          = 1,
            is_superuser       = 0,
            dt_registration    = NOW(),
            progress_dt_start  = NULL, 
            progress_dt_update = NULL
    '''
    values = {
        "email": "user.email",
        "password": "user.password",
        "name": "user.name", 
        "language": "user.language",
    }
    try:
        user_id = await db.execute(query=query, values=values)
        #user_id = "x" ###
        #return {**user.dict(), "id": user_id} # Вообще-то тут еще много полей должно вернуться. Селектить их что ли?
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create user")
    
    return {"message": "Welcome to my FastAPI project!"}


# тут устанавливаем условия подключения к базе данных и отключения - можно использовать в роутах контекстный менеджер async with Database(...) as db: etc
@app.on_event("startup")
async def startup_database():
    await db.connect()
    pass

@app.on_event("shutdown")
async def shutdown_database():
    await db.disconnect()
    pass
    