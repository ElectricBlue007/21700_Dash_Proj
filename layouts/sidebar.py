import dash_bootstrap_components as dbc
from dash import html

sidebar = html.Div(
    [
        html.Div(
            [
                html.H2("Menu", style={"color": "#0374da"}),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fa fa-battery-full"),
                     html.Span(" Batteries")],
                    href="/batteries",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa fa-exclamation-circle"),
                        html.Span(" Reset Errors"),
                    ],
                    href="#",
                    id="reset-errors-link",
                    active="exact",
                ),
                dbc.NavLink(
                    [html.I(className="fa fa-line-chart"),
                     html.Span(" Tables")],
                    href="/tables",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
    style={
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'bottom': 0,
        'width': '205px',
        'padding': '20px',
        'background': 'linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(3,2,74,1) 56%, rgba(0,0,0,1) 100%)',
        'borderRadius': '10px',
        'zIndex': 2
    }
)
