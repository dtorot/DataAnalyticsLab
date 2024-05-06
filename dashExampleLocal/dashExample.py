from flask import Flask

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
 
colors = {
    'background': '#F0F8FF',
    'text': '#00008B'
}

# Our dataframe
df = pd.read_csv('covid_19_india.csv')
 
fig = px.scatter(df, x='Date', y='Confirmed', color='State/UnionTerritory')
fig.update_traces(mode='markers+lines')
 
app.layout = html.Div(children=[
    html.H1(children='COVID-19 Time Series Dashboard'),
 
    html.Div(children='''
        COVID-19 Dashboard: India.
    '''),
 
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)





#app = Flask(__name__)

#@app.route('/')
#def vdata():
#    return 'Aquí van las gráficas'

#app.run(host='localhost', port=5000)
