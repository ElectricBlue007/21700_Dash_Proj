import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Navbar
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("", href="#"),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dcc.Dropdown(
                                id='Process Steps',
                                options=[{'label': 'All Process Step Data', 'value': 'all_process_step_data'}],
                                placeholder="Process Steps",
                                style={'width': '200px', 'margin-right': '50px', "color": "#2C2C2C"}
                            ),
                            className="ml-2"
                        ),
                        dbc.NavItem(
                            dcc.Dropdown(
                                id='Step Type',
                                options=[{'label': 'All', 'value': 'all'}, {'label': 'End', 'value': 'end'}],
                                placeholder="Step Type",
                                style={'width': '120px', 'margin-right': '50px', "color": "#2C2C2C"}
                            ),
                            className="ml-2"
                        ),
                        dbc.NavItem(
                            dcc.Dropdown(
                                id='Process',
                                options=[{'label': 'Process 1', 'value': 'process_1'}, {'label': 'Process 2', 'value': 'process_2'}],
                                placeholder="Process",
                                style={'width': '150px', 'margin-right': '50px', "color": "#2C2C2C"}
                            ),
                            className="ml-2"
                        ),
                    ],
                    className="ml-auto",
                    navbar=True
                ),
                id="navbar-collapse",
                navbar=True
            )
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
    style={"marginLeft": "205px"}
)


main_content = dbc.Row(
    [
        # Sidebar Items
        dbc.Col(
            [
                html.Div(
                    [
                        dbc.Button(
                            "Excel",
                            id="excel-button",
                            color="secondary",
                            className="mb-3",
                            style={"padding": "10px", "width": "60%", "fontSize": "12px"}
                        ),
                        dbc.Button(
                            "Open",
                            id="open-button",
                            color="secondary",
                            className="mb-3",
                            style={"padding": "10px", "width": "60%", "fontSize": "12px"}
                        ),
                        html.Hr(),
                        html.Div(
                            [dbc.ListGroup([dbc.ListGroupItem(f"Battery {i}") for i in range(1, 91)])],
                            style={"overflow-y": "scroll", "height": "500px", "width": "100%"}
                        )
                    ],
                    style={"padding": "20px"}
                )
            ],
            width=2,
            style={"backgroundColor": "#2C2C2C", "padding": "0"}
        ),
        # Main Content Area
        dbc.Col(
            [
                html.Div(id='content'),
                dash_table.DataTable(
                    id='data-table',
                    columns=[
                        {'name': 'Numbers', 'id': 'Numbers'},
                        {'name': 'Type', 'id': 'Type'},
                        {'name': 'Time', 'id': 'Time'},
                        {'name': 'Curr(mA)', 'id': 'Curr(mA)'},
                        {'name': 'Max V(mV)', 'id': 'Max V(mV)'},
                        {'name': 'Min V(mV)', 'id': 'Min V(mV)'},
                        {'name': 'DV(mV)', 'id': 'DV(mV)'},
                        {'name': 'End Curr(mA)', 'id': 'End Curr(mA)'},
                        {'name': 'End Caoa(mAh)', 'id': 'End Caoa(mAh)'},
                        {'name': 'First Step', 'id': 'First Step'},
                        {'name': 'End Step', 'id': 'End Step'},
                        {'name': 'Cycle', 'id': 'Cycle'}
                    ],
                    data=[  # Example data
                        {'Numbers': 1, 'Type': 'A', 'Time': '2024-07-20 12:00:00', 'Curr(mA)': 100, 'Max V(mV)': 4200, 'Min V(mV)': 3400, 'DV(mV)': 800, 'End Curr(mA)': 120, 'End Caoa(mAh)': 1500, 'First Step': 'Start', 'End Step': 'Finish', 'Cycle': 1},
                        {'Numbers': 2, 'Type': 'B', 'Time': '2024-07-20 12:30:00', 'Curr(mA)': 200, 'Max V(mV)': 4300, 'Min V(mV)': 3500, 'DV(mV)': 800, 'End Curr(mA)': 180, 'End Caoa(mAh)': 1600, 'First Step': 'Start', 'End Step': 'Finish', 'Cycle': 2}
                        # Add more rows as needed
                    ],
                    style_table={'overflowX': 'auto'},  # For horizontal scrolling
                    style_header={'backgroundColor': '#2C2C2C', 'color': 'white'},
                    style_data={'color': 'white', 'backgroundColor': '#363636'},
                    style_cell={'textAlign': 'left', 'padding': '5px'},
                )
            ],
            width=10,
            style={"padding": "30px"}
        )
    ]
)

app.layout = html.Div([
    navbar,
    html.Div(
        main_content,
        style={'marginLeft': '205px'}
    )
], style={"backgroundColor": "#2C2C2C", "minHeight": "100vh"})  # Dark background color for the entire page

# Callback to toggle the collapse
@dash.callback(
    dash.dependencies.Output("navbar-collapse", "is_open"),
    [dash.dependencies.Input("navbar-toggler", "n_clicks")],
    [dash.dependencies.State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

dash.register_page(__name__, path="/save-data/cap-save", layout=app.layout)

if __name__ == "__main__":
    app.run_server(debug=True)
