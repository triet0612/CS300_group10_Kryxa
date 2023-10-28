import sqlite3


class DBService:
    def __init__(self, path='./bin/kryxa.db'):
        self.path = path
        self.con: sqlite3.Connection

    def __enter__(self):
        self.con = sqlite3.connect(self.path)
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.con:
            self.con.close()
