from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/template/<name>')
def template(name):
    return render_template(name)

@app.route('/')
def index():
    return render_template('main.html')


if __name__=='__main__':
    app.run()
