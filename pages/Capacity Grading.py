import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_table


layout = html.Div([
    html.Div([
        html.Div([
            html.Div("Config", className='sidebar-button'),
            html.Div("Cool", className='sidebar-button'),
            html.Div("Exceland", className='sidebar-button'),
            html.Div([
                html.Div("Show Grading", className='sidebar-header'),
                dcc.Dropdown(
                    id='gradingDropdown',
                    options=[
                        {'label': 'cp1', 'value': 'cp1'},
                        {'label': 'cp2', 'value': 'cp2'}
                    ],
                    value='cp1',
                    clearable=False,
                    placeholder='Select grading'
                ),
                html.Button('Send', id='sendButton', className='send-button')
            ], className='sidebar-section')
        ], className='sidebar'),

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
                value=[],  # Set the initial value as an empty list for multi-value
                multi=True,  # Enable multi-value selection
                placeholder='Select numbers'
            )
        ], className='main-dashboard')
    ], className='main-container'),

    # Adding the tables
    html.Div([
        # First table
        dash_table.DataTable(
            id='table1',
            columns=[
                {"name": "Sequence", "id": "sequence"},
                {"name": "Sorting Name", "id": "sorting_name"},
                {"name": "Total", "id": "total"},
                {"name": "Quantity", "id": "quantity"},
                {"name": "Percentage", "id": "percentage"}
            ],
            data=[
                {"sequence": 1, "sorting_name": "Alpha", "total": 100, "quantity": 50, "percentage": "50%"},
                {"sequence": 2, "sorting_name": "Beta", "total": 200, "quantity": 150, "percentage": "75%"}
            ],
            style_table={
                'width': '100%',
                'margin': '20px 0',
                'backgroundColor': '#333'  # Dark background for the table
            },
            style_header={
                'backgroundColor': '#444',  # Dark background for the header
                'color': 'white'  # White text for the header
            },
            style_cell={
                'backgroundColor': '#333',  # Dark background for the cells
                'color': 'white'  # White text for the cells
            }
        ),
        # Second table
        dash_table.DataTable(
            id='table2',
            columns=[
                {"name": "Column1", "id": "column1"},
                {"name": "Column2", "id": "column2"},
                {"name": "Column3", "id": "column3"},
                {"name": "Column4", "id": "column4"},
                {"name": "Column5", "id": "column5"}
            ],
            data=[
                {"column1": "Row1-Col1", "column2": "Row1-Col2", "column3": "Row1-Col3", "column4": "Row1-Col4", "column5": "Row1-Col5"},
                {"column1": "Row2-Col1", "column2": "Row2-Col2", "column3": "Row2-Col3", "column4": "Row2-Col4", "column5": "Row2-Col5"}
            ],
            style_table={
                'width': '100%',
                'margin': '20px 0',
                'backgroundColor': '#333'
            },
            style_header={
                'backgroundColor': '#444',
                'color': 'white'
            },
            style_cell={
                'backgroundColor': '#333',
                'color': 'white'
            }
        )
    ], className='tables-container')
], style={'marginLeft': '200px'}
)


@dash.callback(
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


dash.register_page(__name__, path="/operation/cap-gr", layout=layout)
