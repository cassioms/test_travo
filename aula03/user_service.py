import sqlite3

from aula03.user import User

class UserService:

    def __init__(self, dbname):
        self.dbname = dbname
        with sqlite3.connect(dbname) as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS users (id NUMBER, name TEXT, height NUMBER, weight NUMBER)')
            cursor.close()
        conn.close()


    def connected(self, fn, *args):
        with sqlite3.connect(self.dbname) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            results = fn(conn, cursor, *args)
            cursor.close()
        conn.close()
        return results


    def add_user(self, _id, name, height, weight):
        def _add(conn, cursor, _id, name, height, weight):
            cursor.execute('INSERT INTO users VALUES(?, ?, ?, ?)', (_id, name, height, weight,))
            conn.commit()
        self.connected(_add, _id, name, height, weight)


    def update_user(self, _id, name, height, weight):
        def _update(conn, cursor, _id, name, height, weight):
            cursor.execute('UPDATE users SET name = ?, height = ?, weight = ? where id = ?', (name, height, weight, _id,))
            conn.commit()
        self.connected(_update, _id, name, height, weight)


    def delete_user(self, _id):
        def _delete(conn, cursor, _id):
            cursor.execute('DELETE FROM users where id = ?', (_id,))
            conn.commit()
        self.connected(_delete, _id)


    def list_users(self):
        def _list(conn, cursor):
            return self.get_users(cursor)
        return self.connected(_list)


    def get_users(self, cursor):
        cursor.execute('SELECT * FROM users')
        users = list(map(lambda user: User(user), cursor.fetchall()))
        users.sort()
        return list(map(lambda user: user.to_dict(), users))
