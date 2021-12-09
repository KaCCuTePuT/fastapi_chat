import databases
import ormar
import sqlalchemy


metadata = sqlalchemy.MetaData()
database = databases.Database('postgresql://postgres:postgres@localhost/faDb')
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost/faDb')

# database = databases.Database("sqlite:///db.sqlite")
# engine = sqlalchemy.create_engine("sqlite:///db.sqlite")


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
