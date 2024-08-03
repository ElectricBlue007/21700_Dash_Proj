import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

# Layout Definition
layout = html.Div([
    # Main dashboard with buttons and multi-value dropdown
    html.Div([
        html.Div(
            id='dashboard',
            className='dashboard',
            children=[
                html.Div(str(i), id=f'button{i}', className='button') for i in range(1, 91)
            ]
        ),
        dcc.Dropdown(
            id='numberDropdown',
            options=[{'label': str(i), 'value': i} for i in range(1, 91)],
            value=[],
            multi=True,
            placeholder='Select Channels',
            className='dash-dropdown',
        ),

        # Wrap the buttons in a flex container
        html.Div(className='toggle-buttons', children=[
            html.Button('Charge', id='charge-button', className='button'),
            html.Button('Discharge', id='discharge-button', className='button'),
        ]),

        # Modal for Charge Dropdown
        html.Div(
            id='charge-modal',
            className='modal',
            children=[
                html.Div(
                    className='modal-content',
                    children=[
                        dcc.Dropdown(
                            id='chargeDropdown',
                            options=[
                                {'label': 'CC', 'value': 'CC'},
                                {'label': 'CV', 'value': 'CV'},
                                {'label': 'CP', 'value': 'CP'},
                                {'label': 'CR', 'value': 'CR'},
                                {'label': 'Rest', 'value': 'Rest'}
                            ],
                            value=[],  # Set the initial value as an empty list for multi-value
                            multi=True,  # Enable multi-value selection
                            placeholder='Select Charge options',
                            className='dash-dropdown',  # Custom class name
                        ),
                        html.Div(id='charge-inputs'),
                        html.Button('Close', id='close-charge-modal', className='close-button')
                    ]
                )
            ]
        ),

        # Modal for Discharge Dropdown
        html.Div(
            id='discharge-modal',
            className='modal',
            children=[
                html.Div(
                    className='modal-content',
                    children=[
                        dcc.Dropdown(
                            id='dischargeDropdown',
                            options=[
                                {'label': 'CC', 'value': 'CC'},
                                {'label': 'CP', 'value': 'CP'},
                                {'label': 'CR', 'value': 'CR'},
                                {'label': 'Rest', 'value': 'Rest'}
                            ],
                            value=[],  # Set the initial value as an empty list for multi-value
                            multi=True,  # Enable multi-value selection
                            placeholder='Select Discharge options',
                            className='dash-dropdown',  # Custom class name
                        ),
                        html.Div(id='discharge-inputs'),
                        html.Button('Close', id='close-discharge-modal', className='close-button')
                    ]
                )
            ]
        )
    ], className='main-dashboard')
],)

dash.register_page(__name__, path="/sl_chan")

if __name__ == '__main__':
    app.layout = layout
    app.run_server(debug=True, port=20202)