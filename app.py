from flask import Flask

app = Flask(__name__)



@app.route('/')
def home():
    return '<h1>Привіт! Ти можеш відвдіати такі сторінки: /super-buter, /buter-super</h1>'

@app.route('/super-buter')
def about():
    return 'fajslkjdaklsjlkj'

@app.route('/buter-super')
def contact():
    return '<h1>Контакти</h1>'


if __name__ == '__main__':
    app.run(debug=True)