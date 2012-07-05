# -*- coding: utf-8 -*-
""" The main application for Dietzilla.py"""
from flask import Flask, render_template
from datetime import date, datetime, time

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/template/<name>')
def template(name):
    return render_template(name)


@app.route('/')
def index():
    data = {}
    #: Be careful with timezones
    waist = {'title': 'Waist',
             'units': 'inches',
             'data': [[datetime.combine(date(2012, 6, 1), time()), 39.3],
                      [datetime.combine(date(2012, 6, 2), time()), 39.2],
                      [datetime.combine(date(2012, 6, 4), time()), 38.9],
                      [datetime.combine(date(2012, 6, 5), time()), 38.9],
                      [datetime.combine(date(2012, 6, 6), time()), 38.5],
                      [datetime.combine(date(2012, 6, 7), time()), 38.7],
                      [datetime.combine(date(2012, 6, 8), time()), 39.0],
                      [datetime.combine(date(2012, 6, 9), time()), 38.9],
                      [datetime.combine(date(2012, 6, 11), time()), 38.7],
                      [datetime.combine(date(2012, 6, 12), time()), 38.4],
                      [datetime.combine(date(2012, 6, 13), time()), 38.7],
                      [datetime.combine(date(2012, 6, 14), time()), 38.4],
                      [datetime.combine(date(2012, 6, 15), time()), 38.5],
                      [datetime.combine(date(2012, 6, 16), time()), 38.7],
                      [datetime.combine(date(2012, 6, 17), time()), 38.6],
                      [datetime.combine(date(2012, 6, 18), time()), 38.8],
                      [datetime.combine(date(2012, 6, 19), time()), 38.1],
                      [datetime.combine(date(2012, 6, 21), time()), 37.9],
                      [datetime.combine(date(2012, 6, 22), time()), 38.9],
                      [datetime.combine(date(2012, 6, 23), time()), 38.5],
                      [datetime.combine(date(2012, 6, 24), time()), 38.5],
                      [datetime.combine(date(2012, 6, 25), time()), 38.3],
                      [datetime.combine(date(2012, 6, 26), time()), 38.3],
                      [datetime.combine(date(2012, 6, 27), time()), 38.5],
                      [datetime.combine(date(2012, 6, 28), time()), 38.2],
                      [datetime.combine(date(2012, 6, 29), time()), 37.9],
                      [datetime.combine(date(2012, 6, 30), time()), 38.1],
                      [datetime.combine(date(2012, 7, 1), time()), 38.1]
                      ]}
    weight = {'title': 'Weight',
              'units': 'lbs.',
              'data': [[datetime.combine(date(2012, 6, 1), time()), 194.8],
                       [datetime.combine(date(2012, 6, 2), time()), 193.7],
                       [datetime.combine(date(2012, 6, 3), time()), 192.9],
                       [datetime.combine(date(2012, 6, 4), time()), 192.4],
                       [datetime.combine(date(2012, 6, 5), time()), 191.6],
                       [datetime.combine(date(2012, 6, 6), time()), 191.4],
                       [datetime.combine(date(2012, 6, 7), time()), 191.1],
                       [datetime.combine(date(2012, 6, 8), time()), 190.0],
                       [datetime.combine(date(2012, 6, 9), time()), 189.6],
                       [datetime.combine(date(2012, 6, 10), time()), 191.6],
                       [datetime.combine(date(2012, 6, 11), time()), 190.9],
                       [datetime.combine(date(2012, 6, 12), time()), 190.4],
                       [datetime.combine(date(2012, 6, 13), time()), 189.9],
                       [datetime.combine(date(2012, 6, 14), time()), 191.7],
                       [datetime.combine(date(2012, 6, 15), time()), 191.7],
                       [datetime.combine(date(2012, 6, 16), time()), 190.0],
                       [datetime.combine(date(2012, 6, 17), time()), 189.4],
                       [datetime.combine(date(2012, 6, 18), time()), 190.8],
                       [datetime.combine(date(2012, 6, 19), time()), 189.3],
                       [datetime.combine(date(2012, 6, 20), time()), 190.7],
                       [datetime.combine(date(2012, 6, 21), time()), 188.2],
                       [datetime.combine(date(2012, 6, 22), time()), 188.7],
                       [datetime.combine(date(2012, 6, 23), time()), 187.2],
                       [datetime.combine(date(2012, 6, 24), time()), 188.3],
                       [datetime.combine(date(2012, 6, 25), time()), 188.1],
                       [datetime.combine(date(2012, 6, 26), time()), 186.1],
                       [datetime.combine(date(2012, 6, 27), time()), 187.7],
                       [datetime.combine(date(2012, 6, 28), time()), 188.3],
                       [datetime.combine(date(2012, 6, 29), time()), 187.2],
                       [datetime.combine(date(2012, 6, 30), time()), 186.7],
                       [datetime.combine(date(2012, 7, 1), time()), 186.0]
                       ]}

    data['graphs'] = [weight, waist]
    data['initial_days'] = -14
    today = datetime.combine(date.today(), time())
    for dates in data['graphs']:
        data['min_date'] = min(data.get('min_date', datetime.now()),
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
