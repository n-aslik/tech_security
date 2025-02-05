import psycopg

def get_db_connect():
    return psycopg.connect("dbname=tech_securitydb user=postgres  password=@@sl8998 host=localhost port=5432")