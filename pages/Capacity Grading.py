# app.py
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Generate a list of 90 switches
switches = []
for i in range(90):
    switches.append(
        html.Div(
            [
                dcc.Checklist(
                    options=[{'label': '', 'value': f'check-{i}'}],
                    id=f'check-{i}',
                    inline=True,
                    style={'display': 'none'}
                ),
                html.Label(
                    html.I(className='fas fa-power-off'),
                    htmlFor=f'check-{i}',
                    className='switch'
                )
            ],
            className='switch-container'
        )
    )

# Layout of the app
app.layout = html.Div(
    [
        html.Div(switches, className='container')
    ],
    style={'backgroundColor': '#222', 'minHeight': '100vh', 'display': 'grid', 'placeItems': 'center'}
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
