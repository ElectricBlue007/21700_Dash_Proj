import dash
from dash import Dash, dash_table, dcc, html
import pandas as pd
import plotly.graph_objs as go

app = Dash(__name__)

data = {
    "Current": [0.5, 1.0, 1.5, 2.0],
    "Voltage": [3.7, 3.8, 3.9, 4.0],
    "Capacity": [1000, 2000, 3000, 4000],
    "Time": ['2024-07-01 10:00', '2024-07-01 10:10', '2024-07-01 10:20', '2024-07-01 10:30']
}

df = pd.DataFrame(data)

dark_theme = {
    'background': '#303030',
    'text': '#FFFFFF',
    'table_background': '#424242',
    'table_text': '#FFFFFF',
    'graph_background': '#303030',
    'graph_grid': '#606060',
    'graph_text': '#FFFFFF',
    'header_background': '#212121',
    'header_text': '#FFFFFF'
}

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
fig.update_layout(
    paper_bgcolor=dark_theme['graph_background'],
    plot_bgcolor=dark_theme['graph_background'],
    font=dict(color=dark_theme['graph_text']),
    xaxis=dict(gridcolor=dark_theme['graph_grid']),
    yaxis=dict(gridcolor=dark_theme['graph_grid'])
)

tables_layout = html.Div(style={
    'backgroundColor': dark_theme['background'],
    'color': dark_theme['text'],
    'height': '100vh',
    'padding': '20px',
    'marginLeft': '200px'  # Added left margin
}, children=[
    dcc.Graph(
        id='example-graph',
        figure=fig,
        style={'width': '100%', 'height': '600px'}  # Adjust the width and height as needed
    ),
    dash_table.DataTable(
        id='datatable',
        columns=[
            {"name": "Current", "id": "Current"},
            {"name": "Voltage", "id": "Voltage"},
            {"name": "Capacity", "id": "Capacity"},
            {"name": "Time", "id": "Time"}
        ],
        data=df.to_dict('records'),
        style_header={
            'backgroundColor': dark_theme['header_background'],
            'color': dark_theme['header_text']
        },
        style_cell={
            'backgroundColor': dark_theme['table_background'],
            'color': dark_theme['table_text']
        },
        style_table={'overflowX': 'auto'}
    )
])

dash.register_page(__name__, path="/tables", layout=tables_layout)

if __name__ == '__main__':
    app.run_server(debug=True)
