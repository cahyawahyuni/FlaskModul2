from flask import Flask, render_template
from data import data_mpg, data_irit, data_hp
from plots import dist_horsepower, dist_mpg
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def data():
    data= data_mpg().head()
    return render_template('table_data.html', data=data)

@app.route('/stats')
def stats():
    data1 = data_irit()
    data2 = data_hp()
    return render_template('table_stat.html', data=[data1, data2])

@app.route('/plots')
def plots():
    plot1 = dist_mpg()
    plot2 = dist_horsepower()
    return render_template('plots.html', data=[plot1, plot2])

if __name__ == '__main__':
    app.run(debug=True, port=4444)