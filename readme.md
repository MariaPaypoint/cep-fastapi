pip install fastapi uvicorn pymysql python-jose

# fix alembic.ini
pip install alembic
brew install mysql pkg-config
pip install mysqlclient

alembic revision -m "initial migration"
alembic upgrade head

# todo
1. Сделать проверку значений полей в регистрации
2. В MySQL время отстает на 3 часа
3. Select * заменить на поля модели
4. Добавить фильтры в список юзеров
5. Статусы прогресса описать в кейвордах
6. Добавить заморозку прогресса
7. Подумать насчет NULL и NOT NULL
8. Сделать настройку профиля
9. Покрыть тестами