import databases
import ormar
import sqlalchemy


metadata = sqlalchemy.MetaData()
database = databases.Database('postgresql://postgres:postgres@localhost/fadb')
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost/fadb')

# database = databases.Database("sqlite:///db.sqlite")
# engine = sqlalchemy.create_engine("sqlite:///db.sqlite")


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
