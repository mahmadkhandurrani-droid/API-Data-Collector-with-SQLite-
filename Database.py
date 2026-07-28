import sqlite3


class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT
        )
        """)

        self.connection.commit()

    def insert_user(self, user):
        self.cursor.execute(
            """
            INSERT OR REPLACE INTO users
            (id, name, username, email)
            VALUES (?, ?, ?, ?)
            """,
            (
                user["id"],
                user["name"],
                user["username"],
                user["email"]
            )
        )

        self.connection.commit()

    def show_users(self):
        self.cursor.execute("SELECT * FROM users")

        rows = self.cursor.fetchall()

        for row in rows:
            print(row)

    def close(self):
        self.connection.close()
