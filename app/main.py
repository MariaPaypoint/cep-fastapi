from fastapi import FastAPI
from services.users.router import router as users_router
# Импортируйте другие роутеры по мере необходимости

app = FastAPI(title="My FastAPI Project")

# Подключаем роутеры от различных сервисов
app.include_router(users_router, prefix="/service_users", tags=["service_users"])
# Добавьте другие роутеры здесь

@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI project!"}
