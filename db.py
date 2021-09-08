import databases
import ormar
import sqlalchemy


metadata = sqlalchemy.MetaData()
database = databases.Database('postgres://postgres:postgres@localhost/faDb')
engine = sqlalchemy.create_engine('postgres://postgres:postgres@localhost/faDb')


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
