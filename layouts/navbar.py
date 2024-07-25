import dash_bootstrap_components as dbc
from CumFinder import Listed_Ports
import dash

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


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

connect_button = dbc.NavItem(
    dbc.Button("Connect", color="primary", outline=True, className="mr-2", id="connect-button", n_clicks=0)
)

navbar2 = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("", href="/", style={"color": "gray"}),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dropdown_Cum,
                        dropdown_Ports,
                        connect_button,
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
    color="#02000e",
    dark=True,
    style={
        'position': 'fixed',
        'top': 0,
        'left': '207px',
        'right': 0,
        'height': '60px',
        'padding': '10px 20px',
        'borderRadius': '10px',
        'zIndex': 2
    }
)
