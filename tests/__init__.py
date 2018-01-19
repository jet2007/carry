from sqlalchemy import Table, Column, MetaData, ForeignKey, Integer, String, DateTime, create_engine

metadata = MetaData()
users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
    Column('reg_time', DateTime, nullable=False)
)

addresses = Table(
    'addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('users.id')),
    Column('email_address', String, nullable=False, unique=True),
)


class DotDict(dict):
    def __getattr__(self, item):
        return self[item]


class Databases(DotDict):
    def __init__(self, config, **kwargs):
        super(Databases, self).__init__(**kwargs)
        for name in config:
            self[name] = DotDict({
                'name': name,
                'url': config[name],
                'engine': create_engine(config[name])
            })
