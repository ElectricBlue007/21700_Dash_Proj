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
            placeholder='Select numbers to highlight',
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
                                {'label': 'CV', 'value': 'CU'},
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
], style={'marginLeft': '200px'})


@app.callback(
    Output('dashboard', 'children'),
    Input('numberDropdown', 'value')
)
def update_buttons(selected_numbers):
    selected_numbers = selected_numbers or []
    buttons = [
        html.Div(
            str(i),
            id=f'button{i}',
            className='button green' if i in selected_numbers else 'button'
        ) for i in range(1, 91)
    ]
    return buttons


@app.callback(
    [Output('charge-modal', 'style'),
     Output('discharge-modal', 'style')],
    [Input('charge-button', 'n_clicks'),
     Input('discharge-button', 'n_clicks'),
     Input('close-charge-modal', 'n_clicks'),
     Input('close-discharge-modal', 'n_clicks')]
)
def toggle_modal(charge_clicks, discharge_clicks, close_charge_clicks, close_discharge_clicks):
    ctx = dash.callback_context

    if not ctx.triggered:
        return {'display': 'none'}, {'display': 'none'}

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'charge-button':
        return {'display': 'block'}, {'display': 'none'}
    elif button_id == 'discharge-button':
        return {'display': 'none'}, {'display': 'block'}
    elif button_id == 'close-charge-modal':
        return {'display': 'none'}, {'display': 'none'}
    elif button_id == 'close-discharge-modal':
        return {'display': 'none'}, {'display': 'none'}
    else:
        return {'display': 'none'}, {'display': 'none'}


@app.callback(
    Output('charge-inputs', 'children'),
    Input('chargeDropdown', 'value')
)
def update_charge_inputs(selected_options):
    selected_options = selected_options or []
    inputs = []

    if 'CC' in selected_options:
        inputs.extend([
            html.Div([
                html.Label('CC_I'),
                dcc.Input(type='number', id='ch_cc_i', className='input-field')
            ]),
            html.Div([
                html.Label('CC_V-cut'),
                dcc.Input(type='number', id='ch_cc_v_cut', className='input-field')
            ]),
            html.Div([
                html.Label('CC_Time'),
                dcc.Input(type='number', id='ch_cc_t', className='input-field')
            ])
        ])

    if 'CV' in selected_options:
        inputs.extend([
            html.Div([
                html.Label('CV_V'),
                dcc.Input(type='number', id='ch_cv_v', className='input-field')
            ]),
            html.Div([
                html.Label('CV_I-cut'),
                dcc.Input(type='number', id='ch_cv_i_cut', className='input-field')
            ]),
            html.Div([
                html.Label('CV_Time'),
                dcc.Input(type='number', id='ch_cv_t', className='input-field')
            ])
        ])

    if 'CP' in selected_options:
        inputs.extend([
            html.Div([
                html.Label('CP_V-cut'),
                dcc.Input(type='number', id='ch_cp_v_cut', className='input-field')
            ]),
            html.Div([
                html.Label('CP_Current'),
                dcc.Input(type='number', id='ch_cp_cur', className='input-field')
            ]),
            html.Div([
                html.Label('CP_Power'),
                dcc.Input(type='number', id='ch_cp_pow', className='input-field')
            ]),
            html.Div([
                html.Label('CP_Time'),
                dcc.Input(type='number', id='ch_cp_t', className='input-field')

            ])
        ])


    if 'CR' in selected_options:
        inputs.extend([
            html.Div([
                html.Label('CR_R'),
                dcc.Input(type='number', id='ch_cr_r', className='input-field')
            ]),
            html.Div([
                html.Label('CR_V_cut'),
                dcc.Input(type='number', id='ch_cr_v_cut', className='input-field')
            ]),
            html.Div([
                html.Label('CR_I_cut'),
                dcc.Input(type='number', id='ch_cr_i_cut', className='input-field')
            ]),
            html.Div([
                html.Label('CR_Time'),
                dcc.Input(type='number', id='ch_cr_t', className='input-field')
            ])
        ])

    if 'Rest' in selected_options:
        inputs.extend([
            html.Div([
                html.Label('Rest_Time'),
                dcc.Input(type='number', id='ch_rest_t', className='input-field')
            ])
        ])

    return inputs


@app.callback(
    Output('discharge-inputs', 'children'),
    Input('dischargeDropdown', 'value')
)
def update_discharge_inputs(selected_options):
    selected_options = selected_options or []
    inputs = []

    if 'CC' in selected_options:
        inputs.extend([
            html.Div([
                html.Label('CC_Time'),
                dcc.Input(type='number', id='dch_cc_t', className='input-field')
            ]),
            html.Div([
                html.Label('CC_V'),
                dcc.Input(type='number', id='dch_cc_v', className='input-field')
            ]),
            html.Div([
                html.Label('CC_I'),
                dcc.Input(type='number', id='dch_cc_i', className='input-field')
            ])
        ])

    if 'CP' in selected_options:
        inputs.extend([
            html.Div([
                html.Label('CP_V_cut'),
                dcc.Input(type='number', id='dch_cp_v_cut', className='input-field')
            ]),
            html.Div([
                html.Label('CP_Time'),
                dcc.Input(type='number', id='dch_cp_t', className='input-field')
            ]),
            html.Div([
                html.Label('CP_Curr'),
                dcc.Input(type='number', id='dch_cp_cur', className='input-field')
            ]),
            html.Div([
                html.Label('CP_Power'),
                dcc.Input(type='number', id='dch_cp_pow', className='input-field')

            ])
        ])

    if 'CR' in selected_options:
        inputs.extend([
            html.Div([
                html.Label('CR_V_cut'),
                dcc.Input(type='number', id='dch_cr_v_cut', className='input-field')
            ]),
            html.Div([
                html.Label('CR_Time'),
                dcc.Input(type='number', id='dch_cr_t', className='input-field')
            ]),
            html.Div([
                html.Label('CR_I_cut'),
                dcc.Input(type='number', id='dch_cr_i_cut', className='input-field')
            ]),
            html.Div([
                html.Label('CR_R'),
                dcc.Input(type='number', id='dch_cr_r', className='input-field')
            ])
        ])

    if 'Rest' in selected_options:
        inputs.extend([
            html.Div([
                html.Label('Rest_Time'),
                dcc.Input(type='number', id='dch_rest_t', className='input-field')
            ])
        ])

    return inputs



if __name__ == '__main__':
    app.layout = layout
    app.run_server(debug=True)
