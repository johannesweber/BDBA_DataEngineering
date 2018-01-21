# postgreSQL credentials: weber.johanes@gmail.com; test#123
import sqlalchemy


class DBHelper:

    def __init__(self, database):
        self.con, self.meta = self.connect('postgres', 'test#123', database)

    def connect(self, user, password, db, host='localhost', port=5432):
        # We connect with the help of the PostgreSQL URL
        # postgresql://federer:grandestslam@localhost:5432/tennis
        url = 'postgresql://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, db)

        # The return value of create_engine() is our connection object
        con = sqlalchemy.create_engine(url, client_encoding='utf8')

        # We then bind the connection to MetaData()
        meta = sqlalchemy.MetaData(bind=con, reflect=True)

        return con, meta

    def insert(self, entry, tablename):
        table = self.meta.tables[tablename]
        statement = table.insert().values(entry)
        result = self.con.execute(statement)
        return result.inserted_primary_key




