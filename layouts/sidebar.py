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
                        html.I(className="fa fa-bolt"),
                        html.Span(" Charges"),
                    ],
                    href="#",
                    id="charges-toggle",
                    active="exact",
                ),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            html.Div(
                                [
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-battery-full"),
                                            html.Span(" Charging"),
                                        ],
                                        href="/charge/charging",
                                        active="exact"
                                    ),
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-battery-empty"),
                                            html.Span(" DisCharging"),
                                        ],
                                        href="/charge/discharging",
                                        active="exact"
                                    ),
                                ],
                                style={"paddingLeft": "20px"}  # Add indentation
                            )
                        ],
                        vertical=True,
                        pills=True,
                    ),
                    id="charges-collapse",
                    is_open=False,  # Toggle this via callback
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa fa-play-circle"),
                        html.Span(" Actions"),
                    ],
                    href="#",
                    id="actions-toggle",
                    active="exact",
                ),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            html.Div(
                                [
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-play"),
                                            html.Span(" Start"),
                                        ],
                                        href="/action/run",
                                        active="exact"
                                    ),
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-stop"),
                                            html.Span(" Stop"),
                                        ],
                                        href="/action/stop",
                                        active="exact"
                                    ),
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-refresh"),
                                            html.Span(" Restart"),
                                        ],
                                        href="/action/restart",
                                        active="exact"
                                    ),
                                ],
                                style={"paddingLeft": "20px"}  # Add indentation
                            )
                        ],
                        vertical=True,
                        pills=True,
                    ),
                    id="actions-collapse",
                    is_open=False,  # Toggle this via callback
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa fa-save"),
                        html.Span(" Save Data"),
                    ],
                    href="#",
                    id="save-data-toggle",
                    active="exact",
                ),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            html.Div(
                                [
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-save"),
                                            html.Span(" Cap Save"),
                                        ],
                                        href="/save-data/cap-save",
                                        active="exact"
                                    ),
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-database"),
                                            html.Span(" Export Data Collection"),
                                        ],
                                        href="/save-data/export-collection",
                                        active="exact"
                                    ),
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-file-export"),
                                            html.Span(" Export Data Item"),
                                        ],
                                        href="/save-data/export-item",
                                        active="exact"
                                    ),
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-folder-open"),
                                            html.Span(" Open"),
                                        ],
                                        href="/save-data/open",
                                        active="exact"
                                    ),
                                ],
                                style={"paddingLeft": "20px"}  # Add indentation
                            )
                        ],
                        vertical=True,
                        pills=True,
                    ),
                    id="save-data-collapse",
                    is_open=False,  # Toggle this via callback
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa fa-cogs"),
                        html.Span(" Operation"),
                    ],
                    href="#",
                    id="operation-toggle",
                    active="exact",
                ),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            html.Div(
                                [
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-tachometer"),
                                            html.Span(" Capacity Grading"),
                                        ],
                                        href="/operation/cap-gr",
                                        active="exact"
                                    ),
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-calendar"),
                                            html.Span(" Schedule Tasks"),
                                        ],
                                        href="/operation/sch-tasks",
                                        active="exact"
                                    ),
                                    dbc.NavLink(
                                        [
                                            html.I(className="fa fa-cogs"),
                                            html.Span(" Process Step Management"),
                                        ],
                                        href="/operation/p-s-management",
                                        active="exact"
                                    ),
                                ],
                                style={"paddingLeft": "20px"}  # Add indentation
                            )
                        ],
                        vertical=True,
                        pills=True,
                    ),
                    id="operation-collapse",
                    is_open=False,  # Toggle this via callback
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
