import psycopg2

def connection_db():
    return psycopg2.connect(
        dbname='olx_u8',
        user='postgres',
        password='1995',
        host='localhost',
        port=5432
    )
