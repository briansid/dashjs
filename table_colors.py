import dash, random, datetime
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = dash.Dash(__name__)
app.scripts.append_script({"external_url": ['https://code.jquery.com/jquery-3.2.1.min.js',]})

app.layout = dash_table.DataTable(
    id="table",
    data=df.to_dict('rows'),
    columns=[
        {'name': i, 'id': i} for i in df.columns
    ],
    style_data_conditional=[
        {
            'if': {
                'column_id': 'State',
                'filter': 'State eq "California"'
            },
            'backgroundColor': '#3D9970',
            'color': 'white',
        },
        {
            'if': {
                'column_id': 'Humidity',
                'filter': 'Humidity eq num(20)'
            },
            'backgroundColor': '#3D9970',
            'color': 'white',
        },
        {
            'if': {
                'column_id': 'Temperature',
                'filter': 'Temperature > num(3.9)'
            },
            'backgroundColor': '#3D9970',
            'color': 'white',
        },
    ]
)

if __name__ == '__main__':
    app.run_server()