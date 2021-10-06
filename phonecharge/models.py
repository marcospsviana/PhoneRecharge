from datetime import datetime
from decouple import config
from psycopg2 import connect


def connection():
    DB_NAME = config("DB_NAME")
    DB_USER = config("DB_USER")
    DB_PASSWORD = config("DB_PASSWORD")
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT")

    conn = connect(
        database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )
    cursor = conn.cursor()
    return conn, cursor


def conn_close(conn, cursor):
    conn.commit()
    cursor.close()
    conn.close()


def create_all():
    conn, cursor = connection()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS companies(
            id SERIAL,
            public_id VARCHAR(50) NOT NULL,
            name VARCHAR(200) NOT NULL,
            PRIMARY KEY(id));
         CREATE TABLE IF NOT EXISTS products(
            id SERIAL,
            public_id VARCHAR(200) NOT NULL,
            company_id INT NOT NULL,
            value DECIMAL NOT NULL,
            PRIMARY KEY(id),
            CONSTRAINT fk_company
                FOREIGN KEY(company_id)
                    REFERENCES companies(id)
                    ON DELETE RESTRICT);
        CREATE TABLE IF NOT EXISTS recharges(
            id SERIAL,
            public_id VARCHAR(200) NOT NULL,
            product_id INT,
            created_at TIMESTAMP,
            phone_number VARCHAR(15),
            value DECIMAL,
            PRIMARY KEY(id),
            CONSTRAINT fk_product
                FOREIGN KEY(product_id)
                    REFERENCES products(id)
                    ON DELETE RESTRICT
        );
    CREATE TABLE IF NOT EXISTS users(
            id SERIAL,
            email VARCHAR(250) NOT NULL,
            password VARCHAR(300) NOT NULL,
            PRIMARY KEY(id)
        );

    """
    )
    conn_close(conn, cursor)


def save_company(company_id, name):
    conn, cursor = connection()
    sql = f"INSERT INTO companies (public_id, name) VALUES ('{company_id}', '{name}')"
    cursor.execute(sql)
    conn_close(conn, cursor)


def save_products(company_name, public_id, value):
    conn, cursor = connection()
    cursor.execute(f"SELECT id FROM companies WHERE name = '{company_name}';")
    company_id = cursor.fetchall()

    sql = f"INSERT INTO products (public_id, company_id, value) VALUES ('{public_id}', '{company_id[0][0]}', {value})"
    cursor.execute(sql)
    conn_close(conn, cursor)


def save_recharge(public_id, product_public_id, phone_number, value):
    created_at = datetime.isoformat(datetime.now())
    conn, cursor = connection()
    cursor.execute(f"SELECT id FROM products WHERE public_id = '{product_public_id}';")
    product_id = cursor.fetchall()
    sql = f"""INSERT INTO recharges (public_id, product_id, created_at, phone_number, value)\
    VALUES ('{public_id}', {product_id[0][0]}, '{created_at}', '{phone_number}', {value})"""
    cursor.execute(sql)
    conn_close(conn, cursor)


def delete(table, model_data):
    conn, cursor = connection()
    sql = f"DELETE FROM {table} WHERE public_id = '{model_data}'"
    cursor.execute(sql)
    conn_close(conn, cursor)


def get_products():
    conn, cursor = connection()
    sql = "SELECT * FROM products;"
    cursor.execute(sql)
    products = cursor.fetchall()
    conn_close(conn, cursor)
    return products


def get_companies():
    conn, cursor = connection()
    sql = "SELECT * FROM companies;"
    cursor.execute(sql)
    companies = cursor.fetchall()
    conn_close(conn, cursor)
    return companies


def get_recharges():
    conn, cursor = connection()
    sql = "SELECT * FROM recharges;"
    cursor.execute(sql)
    recharges = cursor.fetchall()
    conn_close(conn, cursor)
    return recharges


def init_db():
    create_all()


if __name__ == "__main__":
    init_db()
