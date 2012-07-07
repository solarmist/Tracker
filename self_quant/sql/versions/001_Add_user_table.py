from sqlalchemy import Column, Unicode, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """The user table contains all the information about a user and user_id is
    the basic key upon which all other tables rely.
    """
    __tablename__ = 'account_user'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    email = Column(Unicode, nullable=False)

    def __init(self, user_name, email):
        self.name = user_name
        self.email = email

    def __repr__(self):
        return '<User {} {}>'.format(self.id, self.name)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    Base.metadata.create_all(migrate_engine)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    Base.metadata.drop_all(migrate_engine)
