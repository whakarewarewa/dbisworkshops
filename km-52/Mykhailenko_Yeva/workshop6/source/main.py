import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import json

from flask import Flask, render_template, request, make_response, redirect, session
from wtf.form.html_forms import *
from datetime import datetime, timedelta
from func import *
from vizualization import graph1

app = Flask(__name__)
app.secret_key = 'My_key'
plotly.tools.set_credentials_file(username='whakarewarewa', api_key='4f4aZHi2NsoUo5IIHYpp')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        log_in = request.cookies.get('cookie_name')
        return render_template('authorize.html', log_in=log_in)


@app.route('/graph')
def visualize():
    graph = graph1()
    value = graph.discipline_count()
    print(value)
    disciplines=[]
    counts=[]
    for row in value:
        disciplines+=[row[0]]
        counts+=[row[1]]

    data = go.Bar(x=disciplines, y=counts)
    layout = go.Layout(title='Discipline average mark', xaxis=dict(title='Discipline name'),
                       yaxis=dict(title='Mark',  rangemode='nonnegative', autorange=True))
    data2 = [data]
    fig = go.Figure(data=data2, layout=layout)
    result = py.plot(fig)
    graphJson = json.dumps(data2, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('graphs.html', graphJson=graphJson)


if __name__ == "__main__":
    app.run()
