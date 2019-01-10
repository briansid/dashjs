import dash
import dash_core_components as dcc
import dash_html_components as html
import grasia_dash_components as ddc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.scripts.append_script({"external_url": ['https://code.jquery.com/jquery-3.2.1.min.js',]})

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    ])

if __name__ == '__main__':
    app.run_server()