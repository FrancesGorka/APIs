import psycopg2
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'L4R4isgod'
DATABASE = 'Pagila'
PORT = 5432

with psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DATABASE, port=PORT) as conn:
    with conn.cursor() as cur:
        cur.execute('''CREATE TABLE actor_2 AS (
                    SELECT * FROM actor
                    LIMIT 10);

                    SELECT * FROM actor_2''')
        print(type(cur))
        records = cur.fetchall()