from db import connection_db


def register_user(telegram_id,username):
    connection=connection_db()
    cursor=connection.cursor()
    cursor.execute("""
    INSERT INTO users (telegram_id,username) VALUES (%s,%s)""",(telegram_id,username))
    connection.commit()
    connection.close()

    return None


def get_categories():
    connection=connection_db()
    cursor=connection.cursor()
    cursor.execute("""
    SELECT id,title FROM category""")
    categories = cursor.fetchall()
    connection.close()
    return categories

def check_user(telegram_id,username):
    connection=connection_db()
    cursor=connection.cursor()
    cursor.execute("""
    select telegram_id,username from users where telegram_id=%s and username=%s""",(telegram_id,username))
    user = cursor.fetchone()
    connection.close()
    if user:
        return True
    return False