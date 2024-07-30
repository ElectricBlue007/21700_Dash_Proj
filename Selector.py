import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

# Define layout
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
        html.Div([
            html.Button('Charge', id='charge-button', className='button'),
            html.Button('Discharge', id='discharge-button', className='button'),
        ], className='toggle-buttons'),
        dcc.Dropdown(
            id='chargeDropdown',
            options=[
                {'label': 'CC', 'value': 'CC'},
                {'label': 'CU', 'value': 'CU'},
                {'label': 'CP', 'value': 'CP'},
                {'label': 'CR', 'value': 'CR'},
                {'label': 'Rest', 'value': 'Rest'}
            ],
            value=[],  # Set the initial value as an empty list for multi-value
            multi=True,  # Enable multi-value selection
            placeholder='Select Charge options',
            className='dash-dropdown',  # Custom class name
            style={'display': 'none'}  # Initially hidden
        ),
        dcc.Dropdown(
            id='dischargeDropdown',
            options=[
                {'label': 'CC', 'value': 'CC'},
                {'label': 'CU', 'value': 'CU'},
                {'label': 'CP', 'value': 'CP'},
                {'label': 'CR', 'value': 'CR'},
                {'label': 'Rest', 'value': 'Rest'}
            ],
            value=[],  # Set the initial value as an empty list for multi-value
            multi=True,  # Enable multi-value selection
            placeholder='Select Discharge options',
            className='dash-dropdown',  # Custom class name
            style={'display': 'none'}  # Initially hidden
        )
    ], className='main-dashboard')
], style={'marginLeft': '200px'}
)


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
    [Output('chargeDropdown', 'style'),
     Output('dischargeDropdown', 'style')],
    [Input('charge-button', 'n_clicks'),
     Input('discharge-button', 'n_clicks')]
)
def toggle_dropdown(charge_clicks, discharge_clicks):
    ctx = dash.callback_context

    if not ctx.triggered:
        return {'display': 'none'}, {'display': 'none'}

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'charge-button':
        return {'display': 'block'}, {'display': 'none'}
    elif button_id == 'discharge-button':
        return {'display': 'none'}, {'display': 'block'}
    else:
        return {'display': 'none'}, {'display': 'none'}


if __name__ == '__main__':
    app.layout = layout
    app.run_server(debug=True)
