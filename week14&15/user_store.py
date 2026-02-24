import sqlite3


class UserStore:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER
                )
            """)
            conn.commit()

    def load(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, age FROM users")
            rows = cursor.fetchall()

            users = []
            for row in rows:
                users.append({
                    "id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "age": row[3]
                })
            return users

    def find_by_id(self, user_id: int):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, email, age FROM users WHERE id = ?",
                (user_id,)
            )
            row = cursor.fetchone()

            if row:
                return {
                    "id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "age": row[3]
                }
            return None

    def create_user(self, user_data: dict):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (id, name, email, age)
                VALUES (?, ?, ?, ?)
            """, (
                user_data["id"],
                user_data["name"],
                user_data["email"],
                user_data.get("age")
            ))
            conn.commit()

    def update_user(self, user_id: int, updated_data: dict):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE users
                SET name = ?, email = ?, age = ?
                WHERE id = ?
            """, (
                updated_data["name"],
                updated_data["email"],
                updated_data.get("age"),
                user_id
            ))
            conn.commit()
            return cursor.rowcount > 0

    def delete_user(self, user_id: int):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM users WHERE id = ?",
                (user_id,)
            )
            conn.commit()
            return cursor.rowcount > 0