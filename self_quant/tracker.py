# -*- coding: utf-8 -*-
""" The main application for Dietzilla.py"""
from datetime import date, timedelta, datetime, time
from pytz import timezone
from flask import Flask, render_template, abort
from flask.ext.sqlalchemy import SQLAlchemy
from jinja2 import TemplateNotFound

def setup_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db = SQLAlchemy(app)
    return app, db

app, db = setup_app()

# Needs db to be setup before importing
from .lib.models import Measurement, MeasurementType, User

@app.route('/', defaults={'page': 'index'})
@app.route('/template/<name>')
def show(name):
    try:
        return render_template(name)
    except TemplateNotFound:
        abort(404)

# Insert test data
@app.route('/insert')
def insert():
    from test_data import insert_data
    insert_data()
    return index()

@app.route('/')
def index():
    data = {}
    user = User.query.filter_by(name='Joshua Olson').first()
    m_types = MeasurementType.query.all()
    weight = [m for m in m_types if m.m_name == 'Weight'].pop()
    waist = [m for m in m_types if m.m_name == 'Waist'].pop()
    #: Be careful with timezones to start with all time in GMT
    waist = {'title': str(waist.m_name),
             'units': 'inches',
             'data': Measurement.query.filter_by(user_id=user.id,
                                                 m_type=waist.id).all()}
    waist['data'] = [[m.m_date, m.measurement] for m in waist['data']]
    weight = {'title': str(weight.m_name),
              'units': 'lbs.',
              'data': Measurement.query.filter_by(user_id=user.id,
                                                  m_type=weight.id).all()}
    weight['data'] = [[m.m_date, m.measurement] for m in weight['data']]

    data['graphs'] = [weight, waist]
    data['initial_days'] = -14
    today = datetime.combine(date.today(), time())
    pacific = timezone('US/Pacific')
    now = datetime.now(pacific)
    for dates in data['graphs']:
        data['min_date'] = min(data.get('min_date', now),
                               min([d[0] for d in dates['data']]))
        # Serialize the datetime objects
        for item in dates['data']:
            item[0] = item[0].strftime('%m/%d/%Y %H:%M:%S')
    # data['num_days'] = today-date['min_date']
    # print data['num_days']
    # data['days'] = [d['min_date'] + timedelta(d)
    #                 for d in range(0, data['num_days'])]
    return render_template('main.html', **data)


if __name__ == '__main__':
    app.run()
