import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State  # Import State for storing intermediate values
import serial

from CumFinder import Listed_Ports

dropdown_menu_items = [
    dbc.DropdownMenuItem(ports, id={"type": "port-item", "index": idx}) for idx, ports in enumerate(Listed_Ports)
]

dropdown_Ports = dbc.DropdownMenu(
    dropdown_menu_items,
    label="Serial Port",
    nav=True,
    id="port-dropdown",
)

dropdown_Cum = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem("50", id={"type": "baudrate-item", "index": 50}),
        dbc.DropdownMenuItem("75", id={"type": "baudrate-item", "index": 75}),
        dbc.DropdownMenuItem("110", id={"type": "baudrate-item", "index": 110}),
        dbc.DropdownMenuItem("134", id={"type": "baudrate-item", "index": 134}),
        dbc.DropdownMenuItem("150", id={"type": "baudrate-item", "index": 150}),
        dbc.DropdownMenuItem("200", id={"type": "baudrate-item", "index": 200}),
        dbc.DropdownMenuItem("300", id={"type": "baudrate-item", "index": 300}),
        dbc.DropdownMenuItem("600", id={"type": "baudrate-item", "index": 600}),
        dbc.DropdownMenuItem("1200", id={"type": "baudrate-item", "index": 1200}),
        dbc.DropdownMenuItem("1800", id={"type": "baudrate-item", "index": 1800}),
        dbc.DropdownMenuItem("2400", id={"type": "baudrate-item", "index": 2400}),
        dbc.DropdownMenuItem("4800", id={"type": "baudrate-item", "index": 4800}),
        dbc.DropdownMenuItem("9600", id={"type": "baudrate-item", "index": 9600}),
        dbc.DropdownMenuItem("19200", id={"type": "baudrate-item", "index": 19200}),
        dbc.DropdownMenuItem("28800", id={"type": "baudrate-item", "index": 28800}),
        dbc.DropdownMenuItem("38400", id={"type": "baudrate-item", "index": 38400}),
        dbc.DropdownMenuItem("57600", id={"type": "baudrate-item", "index": 57600}),
        dbc.DropdownMenuItem("76800", id={"type": "baudrate-item", "index": 76800}),
        dbc.DropdownMenuItem("115200", id={"type": "baudrate-item", "index": 115200}),
        dbc.DropdownMenuItem("230400", id={"type": "baudrate-item", "index": 230400}),
        dbc.DropdownMenuItem("460800", id={"type": "baudrate-item", "index": 460800}),
        dbc.DropdownMenuItem("576000", id={"type": "baudrate-item", "index": 576000}),
        dbc.DropdownMenuItem("921600", id={"type": "baudrate-item", "index": 921600}),
    ],
    label="Baud Rate",
    nav=True,
    id="baudrate-dropdown",
)

# Define the Connect button
connect_button = dbc.NavItem(
    dbc.Button("Connect", color="primary", outline=True, className="mr-2", id="connect-button", n_clicks=0)
)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("", href="/", style={"color": "white"}),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dropdown_Cum,
                        dropdown_Ports,
                        connect_button,  # Add the connect_button NavItem here
                    ],
                    navbar=True,
                    className="ml-auto",
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ],
        fluid=True,
    ),
    color="#06131c",
    dark=True,
    style={
        'position': 'fixed',
        'top': 0,
        'left': '200px',
        'right': 0,
        'height': '60px',
        'padding': '10px 20px',
        'borderRadius': '10px',
        'zIndex': 2
    }
)

app.layout = html.Div([navbar, dcc.Store(id='selected-port'), dcc.Store(id='selected-baudrate')])

# Callback to update selected port
@app.callback(
    Output('selected-port', 'data'),
    Input({'type': 'port-item', 'index': dash.dependencies.ALL}, 'n_clicks'),
    [State({'type': 'port-item', 'index': dash.dependencies.ALL}, 'children')],
)
def update_selected_port(n_clicks, port_labels):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        selected_index = eval(button_id)['index']
        return port_labels[selected_index]

# Callback to update selected baudrate
@app.callback(
    Output('selected-baudrate', 'data'),
    Input({'type': 'baudrate-item', 'index': dash.dependencies.ALL}, 'n_clicks'),
    [State({'type': 'baudrate-item', 'index': dash.dependencies.ALL}, 'children')],
)
def update_selected_baudrate(n_clicks, baudrate_labels):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        selected_index = eval(button_id)['index']
        return baudrate_labels[selected_index]


# Callback for handling button click and establishing connection
@app.callback(
    Output("connect-button", "n_clicks"),
    Input("connect-button", "n_clicks"),
    State('selected-port', 'data'),
    State('selected-baudrate', 'data'),
)
def handle_connect(n_clicks, selected_port, selected_baudrate):
    if n_clicks > 0 and selected_port and selected_baudrate:
        try:
            ser = serial.Serial(selected_port, selected_baudrate)
            print(f"Connected to {selected_port} at {selected_baudrate} baud rate")
            # Here you can add additional logic after establishing the connection
        except Exception as e:
            print(f"Failed to connect: {e}")
    return 0  # Reset the click count after handling


if __name__ == "__main__":
    app.run_server(debug=True)
