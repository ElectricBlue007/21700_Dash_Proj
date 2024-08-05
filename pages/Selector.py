import dash
from dash import html, dcc
from dash.dash_table import DataTable
import callbacks  # Import the callbacks module

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

dark_theme = {
    'background': '#303030',
    'text': '#FFFFFF',
    'table_background': '#0386723A',
    'table_text': '#000115FF',
    'header_background': '#035C863A',
    'header_text': '#000115FF'
}

# Initial data for the DataTable
initial_data = [
    {f'column{i}': f'{i}' for i in range(1, 11)},
    {f'column{i}': f'{i*2}' for i in range(1, 11)},
    {f'column{i}': f'{i*3}' for i in range(1, 11)}
]

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

        html.Div(className='toggle-buttons', children=[
            html.Button('Charge', id='charge-button', className='ch-button'),
            html.Button('Discharge', id='discharge-button', className='dch-button'),
        ]),

        html.Div(className='toggle-buttons', children=[
            html.Button('Done', id='done-button', className='done-button'),
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
                        html.Button('Close', id='close-charge-modal', className='close-button'),
                        html.Button('OK', id='ok-charge-modal', className='ok-button')
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
                        html.Button('Close', id='close-discharge-modal', className='close-button'),
                        html.Button('OK', id='ok-discharge-modal', className='ok-button')

                    ]
                )
            ]
        ),
        # Add DataTable with columns named Column1 to Column10
        html.Div(
            id='data-table',
            className='data-table',
            children=[
                DataTable(
                    id='datatable',
                    columns=[{'name': f'Column{i}', 'id': f'column{i}'} for i in range(1, 11)],
                    data=initial_data,
                    style_header={
                        'backgroundColor': dark_theme['header_background'],
                        'color': dark_theme['header_text']
                    },
                    style_cell={
                        'backgroundColor': dark_theme['table_background'],
                        'color': dark_theme['table_text']
                    },
                    style_table={'overflowX': 'auto'}
                )
            ]
        )
    ], className='main-dashboard')
], style={
    'marginLeft': '320px',
    'padding': '-10px'
})

dash.register_page(__name__, path="/sl_chan")

if __name__ == '__main__':
    app.layout = layout
    app.run_server(debug=True, port=20202)
