import plotly
from data import data_mpg
import json
import plotly.express as px

def dist_mpg():
    df = data_mpg()
    fig = px.histogram(df, x="mpg", marginal="rug")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) #ubah ke json biar bisa dipake di html
    return fig_json 
   

def dist_horsepower():
    df = data_mpg()
    fig = px.histogram(df, x="horsepower", marginal="rug")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) #ubah ke json biar bisa dipake di html
    return fig_json 
