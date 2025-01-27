import psycopg
from os import getenv

HOST=getenv("host")
PORT=getenv("port")
USER=getenv("user")
PASSWORD=getenv("password")
DBNAME=getenv("dbname")
def get_db_connect():
    return psycopg.connect(host=HOST,port=PORT,user=USER,password=PASSWORD,database=DBNAME)