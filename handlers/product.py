from db import connection_db


def cat_all_product_view(cat_id):
    connection=connection_db()
    cursor=connection.cursor()
    cursor.execute("select * from product where cat=%s",(cat_id,))
    products=cursor.fetchall()
    product=[product for product in products]
    return product


def order_product(id,username):
    connection=connection_db()
    cursor=connection.cursor()
    product_id=cursor.execute("select id from product where id=%s",(id,))
    user_id=cursor.execute("select id from product where id=%s",(username,))
    cursor.execute("""
    insert into orders (client,product)
    values (%s,%s)""",(user_id,product_id))
    connection.commit()
    connection.close()

    return True