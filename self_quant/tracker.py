from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/template/<name>')
def template(name):
    return render_template(name)

@app.route('/')
def index():
    template_data = {}
    waist = {'title': 'Waist',
             'units': 'inches',
             'data':[['06/15/2012', 38.5],
                     ['06/16/2012', 38.7],
                     ['06/17/2012', 38.6],
                     ['06/18/2012', 38.8],
                     ['06/19/2012', 38.1],
                     ['06/21/2012', 37.9],
                     ['06/22/2012', 38.9],
                     ['06/23/2012', 38.5],
                     ['06/24/2012', 38.5],
                     ['06/25/2012', 38.3]
                     ]}
    weight = {'title': 'Weight',
              'units': 'lbs.',
              'data':[['06/15/2012', 191.7],
                      ['06/16/2012', 190.0],
                      ['06/17/2012', 189.4],
                      ['06/18/2012', 190.8],
                      ['06/19/2012', 189.3],
                      ['06/20/2012', 190.7],
                      ['06/21/2012', 188.2],
                      ['06/22/2012', 188.7],
                      ['06/23/2012', 187.2],
                      ['06/24/2012', 188.3],
                      ['06/25/2012', 186.6]
                             ]};

    template_data['graphs'] = [weight, waist]
    return render_template('main.html', **template_data)


if __name__=='__main__':
    app.run()
