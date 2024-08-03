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
    className="sidebar"
)
