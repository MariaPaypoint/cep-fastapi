pip install fastapi uvicorn pymysql python-jose

# fix alembic.ini
pip install alembic
brew install mysql pkg-config
pip install mysqlclient

alembic revision -m "initial migration"
alembic upgrade head
