from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Unicode, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base()


class MeasurementType(Base):
    """Define what types of measurements are available."""
    __tablename__ = 'measurement_type'
    id = Column(Integer, primary_key=True)
    m_name = Column(Unicode, nullable=False, unique=True)

    def __init__(self, m_name):
        self.m_name = m_name


class Measurement(Base):
    """This table contains all measurements that are going to be recorded."""
    __tablename__ = 'measurement'
    user_id = Column(Integer, ForeignKey('account_user.id'), primary_key=True)
    m_type = Column(Integer, ForeignKey('measurement_type.id'),
                    primary_key=True)
    m_date = Column(DateTime(timezone=True),
                    nullable=False, primary_key=True)
    measurement = Column(Float, nullable=False, primary_key=True)

    m_type_name = relationship('MeasurementType')


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    Session = sessionmaker(bind=migrate_engine)
    Base.metadata.bind = migrate_engine

    class User(Base):
        __tablename__ = 'account_user'
        __table_args__ = {'autoload': True}

    Measurement.user = relationship(
        'User',
        backref=backref('measurements',
                        order_by=Measurement.m_date,
                        lazy='dynamic'))

    Base.metadata.create_all()

    # Add initial types
    session = Session()
    session.add_all([MeasurementType('Weight'),
                     MeasurementType('Height'),
                     MeasurementType('Waist')])
    session.commit()
    session.close()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    Base.metadata.bind = migrate_engine
    Base.metadata.tables['measurement'].drop()
    Base.metadata.tables['measurement_type'].drop()
