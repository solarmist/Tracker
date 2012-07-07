from pytz import utc
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, Unicode, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from self_quant.tracker import db


class User(db.Model):
    """The user table contains all the information about a user and user_id is
    the basic key upon which all other tables rely.
    """
    __tablename__ = 'account_user'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    email = Column(Unicode, nullable=False)

    def __init(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User {} <{}> ({})>'.format(self.name, self.email, self.id)


class MeasurementType(db.Model):
    """Define what types of measurements are available."""
    __tablename__ = 'measurement_type'
    id = Column(Integer, primary_key=True)
    m_name = Column(Unicode, nullable=False, unique=True)

    def __init__(self, m_name):
        self.m_name = m_name

    def __repr__(self):
        return "<MeasurementType('{}')>".format(self.m_name)


class Measurement(db.Model):
    """This table contains all measurements that are going to be recorded."""
    __tablename__ = 'measurement'
    user_id = Column(Integer, ForeignKey('account_user.id'), primary_key=True)
    m_type = Column(Integer, ForeignKey('measurement_type.id'),
                    primary_key=True)
    m_date = Column(DateTime(timezone=True), nullable=False, primary_key=True)
    measurement = Column(Float, nullable=False, primary_key=True)

    m_type_name = relationship('MeasurementType')
    user = relationship('User',
                        backref=backref('measurements',
                                        order_by=m_date,
                                        lazy='dynamic'))

    def __init__(self, user, m_type, datetime, measurement):
        self.user_id = user.id if isinstance(user, User) else user
        self.m_type = m_type.id if isinstance(m_type,
                                            MeasurementType) else m_type
        self.m_date = datetime.astimezone(utc)
        self.measurement = measurement

    def __repr__(self):
        return '<Measurement {}, {}, {}, {}>'.format(self.user_id,
                                                     self.m_date,
                                                     self.m_type,
                                                     self.measurement)
