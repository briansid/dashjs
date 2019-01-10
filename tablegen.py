import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([html.Thead(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])]),

        # Body
        html.Tbody([html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))])
    ],
    id="table")


external_stylesheets = ['https://cdn.datatables.net/1.10.19/css/jquery.dataTables.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.scripts.append_script({"external_url": [
    'https://code.jquery.com/jquery-3.2.1.min.js',
    'https://cdn.datatables.net/1.10.19/js/jquery.dataTables.js'
    ]})

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server()