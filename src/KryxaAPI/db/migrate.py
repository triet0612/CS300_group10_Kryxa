from db.database import DBService

if __name__ == '__main__':
    with open('./design.sql', 'r') as design_file:
        script = design_file.read()
        with DBService('../bin/kryxa.db') as cur:
            cur.executescript(script)
