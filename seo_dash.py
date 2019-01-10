import dash, random, datetime
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd


global_data = []

columns=[
    'Domain',
    'Traffic',
    'FD',
    'PKH',
    'UPTime',
    'Speed Test',
    'SERP Desktop',
    'SERP Mobile',
    'Links',
    'Content',
    'Robots',
    'Y.Alert',
    'G.Alert',
    'Exp. Date',
    'Pages',
    'Y.Index',
    'G.Index',
]

external_stylesheets = ['https://cdn.datatables.net/1.10.19/css/jquery.dataTables.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.scripts.append_script({"external_url": [
    'https://code.jquery.com/jquery-3.2.1.min.js',
    'https://cdn.datatables.net/1.10.19/js/jquery.dataTables.js'
    ]})

app.layout = html.Div([
    dash_table.DataTable(
        id='datatable',
        # css={"selector": ".table .thead-dark"},
        style_table={
            'class': 'table thead-dark'
        },
        style_header={
            'className': 'thead-dark'
        },
        columns=[{"name": i, "id": i} for i in columns],
        data=[],
        style_data_conditional=[
            {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
            },
            {
            'if': {
                'column_id': 'PKH',
                'filter': 'PKH eq "site"'
            },
            'backgroundColor': '#ff1414',
            'color': 'white',
             },
             {
            'if': {
                'column_id': 'PKH',
                'filter': 'PKH eq "site 192.168.0.1"'
            },
            'backgroundColor': '#ff1414',
            'color': 'white',
             },
        ],
        style_cell_conditional=[
        {'if': {'column_id': 'PKH'},
         'width': '135px'},
    ],
    # virtualization=True,
    pagination_mode=False,
    # filtering=True,
    ),
    dcc.Interval(
            id='interval-component',
            interval=1*3000, # in milliseconds
            n_intervals=0
    ),
    html.Div(id='container', className="lert alert-danger")
],)


@app.callback(Output('datatable', 'data'),
              [Input('interval-component', 'n_intervals'),])
def update_metrics(n):
    global global_data
    old_data = global_data

    if old_data != []:
        for row in old_data:
            try:
                row['Traffic'] = int(row['Traffic'].replace('▼', '').replace('▲', ''))
            except AttributeError:
                pass
            try:
                row['FD'] = int(row['FD'].replace('▼', '').replace('▲', ''))
            except AttributeError:
                pass


    new_data = []
    for i in range(1,15):
        new_data.append({
            'Domain': 'ww' +str(i),
            'Traffic': random.choice([i for i in range(0,11000, 1000)]),
            'FD': random.choice([i for i in range(0,110,10)]),
            'PKH': random.choice(['ok', 'site', '192.168.0.1', 'site 192.168.0.1']),
            'UPTime': random.choice([0, 200]),
            'Speed Test': random.choice([1, 2, 3, 4]),
            'SERP Desktop': random.randint(0,250),
            'SERP Mobile': random.randint(0,250),
            'Links': random.randint(0,60),
            'Content': random.choice(['ok', 'change']),
            'Robots': random.choice(['ok', 'change']),
            'Y.Alert': random.choice(['ok', 'change']),
            'G.Alert': random.choice(['ok', 'change']),
            'Exp. Date': '02.05.21',
            'Pages': random.randint(0,500),
            'Y.Index': random.randint(0,500),
            'G.Index': random.randint(0,500),
            })

    global_data = new_data

    if old_data == []:
        return new_data

    # Make for loop for all rows
    for index, row in enumerate(new_data):
        # Traffic
        if new_data[index]['Traffic'] < old_data[index]['Traffic']:
            new_data[index]['Traffic'] = str(new_data[index]['Traffic']) + ' ▼'
        elif new_data[index]['Traffic'] > old_data[index]['Traffic']:
            new_data[index]['Traffic'] = str(new_data[index]['Traffic']) + ' ▲'
        # FD
        if new_data[index]['FD'] < old_data[index]['FD']:
            new_data[index]['FD'] = str(new_data[index]['FD']) + ' ▼'
        elif new_data[index]['FD'] > old_data[index]['FD']:
            new_data[index]['FD'] = str(new_data[index]['FD']) + ' ▲'

    return new_data


# @app.callback(Output('container', 'children'),
#               [Input('datatable', 'data')])
# def alert(data):
#     alert_sites = []
#     for n, d in enumerate(data):
#         if d['PKH'] == "site" or d['PKH'] == "site 192.168.0.1":
#             alert_sites.append(d['Domain'])
#     return html.Div('PKH ALERT: %s' % ', '.join(alert_sites), style={'color': 'black'})


if __name__ == '__main__':
    app.run_server()