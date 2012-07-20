from datetime import datetime
from pytz import timezone
from sqlalchemy.exc import IntegrityError
from self_quant.lib.models import User, Measurement, MeasurementType
from self_quant.tracker import db, app


def insert_data():

    user = User.query.filter_by(name='Joshua Olson').first()
    if not user:
        user = User(name='Joshua Olson', email='joshua.olson@gmail.com')
        db.session.add(user)
        db.session.commit()

    m_types = MeasurementType.query.all()
    d_to_ts = lambda y, m, d: datetime(y, m, d, 0, 0,
                                       tzinfo=timezone('US/Pacific'))
    weight = [m for m in m_types if m.m_name == 'Weight'].pop()
    waist = [m for m in m_types if m.m_name == 'Waist'].pop()

    # Insert waist measurements
    measurements = [Measurement(user, waist, d_to_ts(2012, 6, 1), 39.3),
                    Measurement(user, waist, d_to_ts(2012, 6, 2), 39.2),
                    Measurement(user, waist, d_to_ts(2012, 6, 4), 38.9),
                    Measurement(user, waist, d_to_ts(2012, 6, 5), 38.9),
                    Measurement(user, waist, d_to_ts(2012, 6, 6), 38.5),
                    Measurement(user, waist, d_to_ts(2012, 6, 7), 38.7),
                    Measurement(user, waist, d_to_ts(2012, 6, 8), 39.0),
                    Measurement(user, waist, d_to_ts(2012, 6, 9), 38.9),
                    Measurement(user, waist, d_to_ts(2012, 6, 11), 38.7),
                    Measurement(user, waist, d_to_ts(2012, 6, 12), 38.4),
                    Measurement(user, waist, d_to_ts(2012, 6, 13), 38.7),
                    Measurement(user, waist, d_to_ts(2012, 6, 14), 38.4),
                    Measurement(user, waist, d_to_ts(2012, 6, 15), 38.5),
                    Measurement(user, waist, d_to_ts(2012, 6, 16), 38.7),
                    Measurement(user, waist, d_to_ts(2012, 6, 17), 38.6),
                    Measurement(user, waist, d_to_ts(2012, 6, 18), 38.8),
                    Measurement(user, waist, d_to_ts(2012, 6, 19), 38.1),
                    Measurement(user, waist, d_to_ts(2012, 6, 21), 37.9),
                    Measurement(user, waist, d_to_ts(2012, 6, 22), 38.9),
                    Measurement(user, waist, d_to_ts(2012, 6, 23), 38.5),
                    Measurement(user, waist, d_to_ts(2012, 6, 24), 38.5),
                    Measurement(user, waist, d_to_ts(2012, 6, 25), 38.3),
                    Measurement(user, waist, d_to_ts(2012, 6, 26), 38.3),
                    Measurement(user, waist, d_to_ts(2012, 6, 27), 38.5),
                    Measurement(user, waist, d_to_ts(2012, 6, 28), 38.2),
                    Measurement(user, waist, d_to_ts(2012, 6, 29), 37.9),
                    Measurement(user, waist, d_to_ts(2012, 6, 30), 38.1),
                    Measurement(user, waist, d_to_ts(2012, 7, 1), 38.1),
                    Measurement(user, waist, d_to_ts(2012, 7, 2), 38.1),
                    Measurement(user, waist, d_to_ts(2012, 7, 3), 37.8),
                    Measurement(user, waist, d_to_ts(2012, 7, 4), 38.3),
                    Measurement(user, waist, d_to_ts(2012, 7, 5), 38.2),
                    Measurement(user, waist, d_to_ts(2012, 7, 6), 38.0),
                    Measurement(user, waist, d_to_ts(2012, 7, 7), 38.0),
                    Measurement(user, waist, d_to_ts(2012, 7, 8), 37.8),
                    Measurement(user, waist, d_to_ts(2012, 7, 9), 38.1),
                    Measurement(user, waist, d_to_ts(2012, 7, 10), 37.7),
                    Measurement(user, waist, d_to_ts(2012, 7, 11), 37.8),

                    Measurement(user, waist, d_to_ts(2012, 7, 12), 37.7),
                    Measurement(user, waist, d_to_ts(2012, 7, 13), 37.9),
                    Measurement(user, waist, d_to_ts(2012, 7, 14), 37.7),
                    Measurement(user, waist, d_to_ts(2012, 7, 15), 37.8),
                    Measurement(user, waist, d_to_ts(2012, 7, 16), 37.8),
                    Measurement(user, waist, d_to_ts(2012, 7, 17), 37.8),
                    Measurement(user, waist, d_to_ts(2012, 7, 18), 37.8),
                    Measurement(user, waist, d_to_ts(2012, 7, 19), 37.8),
                    # Insert weight measurements
                    Measurement(user, weight, d_to_ts(2012, 6, 1), 194.8),
                    Measurement(user, weight, d_to_ts(2012, 6, 2), 193.7),
                    Measurement(user, weight, d_to_ts(2012, 6, 3), 192.9),
                    Measurement(user, weight, d_to_ts(2012, 6, 4), 192.4),
                    Measurement(user, weight, d_to_ts(2012, 6, 5), 191.6),
                    Measurement(user, weight, d_to_ts(2012, 6, 6), 191.4),
                    Measurement(user, weight, d_to_ts(2012, 6, 7), 191.1),
                    Measurement(user, weight, d_to_ts(2012, 6, 8), 190.0),
                    Measurement(user, weight, d_to_ts(2012, 6, 9), 189.6),
                    Measurement(user, weight, d_to_ts(2012, 6, 10), 191.6),
                    Measurement(user, weight, d_to_ts(2012, 6, 11), 190.9),
                    Measurement(user, weight, d_to_ts(2012, 6, 12), 190.4),
                    Measurement(user, weight, d_to_ts(2012, 6, 13), 189.9),
                    Measurement(user, weight, d_to_ts(2012, 6, 14), 191.7),
                    Measurement(user, weight, d_to_ts(2012, 6, 15), 191.7),
                    Measurement(user, weight, d_to_ts(2012, 6, 16), 190.0),
                    Measurement(user, weight, d_to_ts(2012, 6, 17), 189.4),
                    Measurement(user, weight, d_to_ts(2012, 6, 18), 190.8),
                    Measurement(user, weight, d_to_ts(2012, 6, 19), 189.3),
                    Measurement(user, weight, d_to_ts(2012, 6, 20), 190.7),
                    Measurement(user, weight, d_to_ts(2012, 6, 21), 188.2),
                    Measurement(user, weight, d_to_ts(2012, 6, 22), 188.7),
                    Measurement(user, weight, d_to_ts(2012, 6, 23), 187.2),
                    Measurement(user, weight, d_to_ts(2012, 6, 24), 188.3),
                    Measurement(user, weight, d_to_ts(2012, 6, 25), 188.1),
                    Measurement(user, weight,
                                datetime(2012, 6, 26, 9, 05,
                                         tzinfo=timezone('US/Pacific')),
                                186.5),
                    Measurement(user, weight, d_to_ts(2012, 6, 26), 186.1),
                    Measurement(user, weight, d_to_ts(2012, 6, 27), 187.7),
                    Measurement(user, weight, d_to_ts(2012, 6, 28), 188.3),
                    Measurement(user, weight, d_to_ts(2012, 6, 29), 187.2),
                    Measurement(user, weight, d_to_ts(2012, 6, 30), 186.7),
                    Measurement(user, weight, d_to_ts(2012, 7, 1), 186.0),
                    Measurement(user, weight, d_to_ts(2012, 7, 2), 185.5),
                    Measurement(user, weight, d_to_ts(2012, 7, 3), 186.0),
                    Measurement(user, weight, d_to_ts(2012, 7, 4), 185.7),
                    Measurement(user, weight, d_to_ts(2012, 7, 5), 187.8),
                    Measurement(user, weight, d_to_ts(2012, 7, 6), 186.6),
                    Measurement(user, weight, d_to_ts(2012, 7, 7), 185.3),
                    Measurement(user, weight, d_to_ts(2012, 7, 8), 187.3),
                    Measurement(user, weight,
                                datetime(2012, 7, 7, 11, 10,
                                         tzinfo=timezone('US/Pacific')),
                                185.4)
                    Measurement(user, weight, d_to_ts(2012, 7, 8), 187.3),
                    Measurement(user, weight, d_to_ts(2012, 7, 9), 186.6),
                    Measurement(user, weight, d_to_ts(2012, 7, 10), 185.7),
                    Measurement(user, weight, d_to_ts(2012, 7, 11), 186.1),
                    Measurement(user, weight, d_to_ts(2012, 7, 12), 185.5),
                    Measurement(user, weight, d_to_ts(2012, 7, 13), 185.7),
                    Measurement(user, weight, d_to_ts(2012, 7, 14), 184.9),
                    Measurement(user, weight, d_to_ts(2012, 7, 15), 185.8),
                    Measurement(user, weight, d_to_ts(2012, 7, 16), 187.4),
                    Measurement(user, weight, d_to_ts(2012, 7, 17), 184.7),
                    Measurement(user, weight, d_to_ts(2012, 7, 18), 186.2),
                    Measurement(user, weight, d_to_ts(2012, 7, 19), 188.2),
                    Measurement(user, weight, d_to_ts(2012, 7, 20), 187.4),
                    ]

    for measurement in measurements:
        try:
            db.session.add(measurement)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            app.logger.error('Rolling back waist data: {}', measurement)
