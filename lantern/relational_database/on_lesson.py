from pprint import pprint
import psycopg2


conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='foo',
    host='localhost',
    port=5432
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM users;')
pprint(cursor.fetchall())


cursor.execute(
    """
    INSERT INTO users (name, surname, money)
    VALUES (%s, %s, %s)
    """,
    ('Vasya', 'Pupkin', 0))

cursor.execute('SELECT * FROM users;')
pprint(cursor.fetchall())
# conn.commit()


values = {
    'first_name': 'Ivan',
    'surname': 'Solopenko',
    'cash': 1500}

cursor.execute(
    """
    INSERT INTO users (name, surname, money)
    VALUES (%(first_name)s, %(surname)s, %(cash)s)
    """,
    values)

cursor.execute('SELECT * FROM users;')
pprint(cursor.fetchall())
# conn.commit()

