import dash
# give style to html in dash
from dash import html, dcc
# callbacks modules
from dash.dependencies import Input, Output, State
# connect html to dash
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
import serial
# import navbar from directory layout
from layouts.navbar import navbar2
import time

# HTML template for displaying battery information
battery_html_template = '''
<section class="battery">
    <b><div class="battery__card glass" style="width: 150px; height: 180px; border: 1px solid rgba(82, 63, 233, 0.60); position: relative; margin: 2px;">
        <div class="battery__data">
            <h1 class="battery__percentage" style="font-size: 16px; margin-bottom: 2px; line-height: 1;">{percentage}%</h1>
            <p class="battery__status" style="font-size: 10px; margin-bottom: 2px; line-height: 1;">{status}</p>
            <p class="battery__extra" style="font-size: 10px; margin-bottom: 2px; line-height: 1;">V: {V}</p>
            <p class="battery__extra" style="font-size: 10px; margin-bottom: 2px; line-height: 1;">I: {I}</p>
            <p class="battery__extra" style="font-size: 10px; margin-bottom: 2px; line-height: 1;">Time: {step_time}</p>
            <p class="battery__extra" style="font-size: 10px; margin-bottom: 2px; line-height: 1;">Num: {step_num}</p>
            <p class="battery__extra" style="font-size: 10px; margin-bottom: 2px; line-height: 1;">Err: {error}</p>
            <p class="battery__extra" style="font-size: 10px; margin-bottom: 2px; line-height: 1;">Type: {step_type}</p></b>
        </div>
        <div class="battery__pill">
            <div class="battery__level">
                <div class="battery__liquid" style="height: {liquid_height}%; background: {liquid_color};"></div>
            </div>
        </div>
        <div class="battery__num" style="position: absolute; bottom: 5px; right: 5px; font-size: 10px; font-weight: bold;">{num}</div>
    </div>
</section>
'''

# Initial battery data for 90 batteries
initial_battery_data = [
    {'percentage': 0, 'status': '', 'liquid_color': '',
     'num': i + 1, 'V': 0, 'I': 0, 'step_time': 0, 'step_num': 0, 'error': 0, 'step_type': 0
    } for i in range(90)
]

# battery status and color based on percentage
def get_battery_status_and_color(percentage):
    if percentage <= 20:
        return "", 'linear-gradient(90deg, hsl(7, 89%, 46%) 15%, hsl(11, 93%, 68%) 100%)'
    elif percentage <= 40:
        return "", 'linear-gradient(90deg, hsl(22, 89%, 46%) 15%, hsl(54, 90%, 45%) 100%)'
    elif percentage <= 80:
        return "", 'linear-gradient(90deg, hsl(54, 89%, 46%) 15%, hsl(92, 90%, 45%) 100%)'
    else:
        return "", 'linear-gradient(90deg, hsl(92, 89%, 46%) 15%, hsl(92, 90%, 68%) 100%)'

# Layout for the Dash app
layout = html.Div(
    id='page-content',
    className="content",
    style={
        'marginLeft': '200px',
        'marginTop': '-20px',
        'padding': '10px',
        'background': 'linear-gradient(356deg, rgba(0,0,0,1) 0%, rgba(6,1,61,1) 57%, rgba(0,0,0,1) 100%), rgb(0,0,0)'
    },
    children=[
        navbar2,
        dcc.Store(id='battery-store', data=initial_battery_data),
        html.Div(id='battery-components'),
        html.Div(
            [
                dcc.Dropdown(
                    id='battery-selector',
                    options=[{'label': f'Battery {i}', 'value': i} for i in range(1, 91)],
                    placeholder='Select a battery to update',
                    style={'margin': '5px', 'backgroundColor': 'white', 'color': 'black'}
                ),
                dcc.Input(id='battery-input', type='number', min=0, max=100, step=1, value=20, style={'padding': '5px'}),
                dcc.Input(id='V-input', type='number', placeholder='V', style={'margin': '5px'}),
                dcc.Input(id='I-input', type='number', placeholder='I', style={'margin': '5px'}),
                dcc.Input(id='step-time-input', type='number', placeholder='Time', style={'margin': '5px'}),
                dcc.Input(id='step-num-input', type='number', placeholder='Num', style={'margin': '5px'}),
                dcc.Input(id='error-input', type='text', placeholder='Err', style={'margin': '5px'}),
                dcc.Input(id='step-type-input', type='text', placeholder='Type', style={'margin': '5px'}),
                html.Button('Update Battery', id='update-button', n_clicks=0, style={'margin': '5px'})
            ],
            style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center', 'alignItems': 'center'}
        )
    ]
)

# Callback to update battery data
@dash.callback(
    Output('battery-store', 'data'),
    Input('update-button', 'n_clicks'),
    [
        State('battery-store', 'data'),
        State('battery-selector', 'value'),
        State('battery-input', 'value'),
        State('V-input', 'value'),
        State('I-input', 'value'),
        State('step-time-input', 'value'),
        State('step-num-input', 'value'),
        State('error-input', 'value'),
        State('step-type-input', 'value')
    ]
)
def update_battery_store(n_clicks, battery_data, selected_battery, battery_percentage, V, I, step_time, step_num, error, step_type):
    if selected_battery is not None and battery_percentage is not None:
        status, color = get_battery_status_and_color(battery_percentage)
        battery_data[selected_battery - 1] = {
            'percentage': battery_percentage,
            'status': status,
            'liquid_color': color,
            'num': selected_battery,
            'V': V,
            'I': I,
            'step_time': step_time,
            'step_num': step_num,
            'error': error,
            'step_type': step_type
        }
    return battery_data

# Callback to update battery components on the page
@dash.callback(
    Output('battery-components', 'children'),
    Input('battery-store', 'data')
)
def update_battery_components(battery_data):
    battery_components = []
    for index in range(90):
        battery = battery_data[index]
        battery_html = battery_html_template.format(
            percentage=battery['percentage'],
            status=battery['status'],
            liquid_height=battery['percentage'],
            liquid_color=battery['liquid_color'],
            num=battery['num'],
            V=battery['V'],
            I=battery['I'],
            step_time=battery['step_time'],
            step_num=battery['step_num'],
            error=battery['error'],
            step_type=battery['step_type']
        )
        battery_components.append(html.Div(
            DangerouslySetInnerHTML(battery_html),
            style={'margin': '10px', 'padding': '15px', 'flexBasis': '150px'}
        ))
    return html.Div(battery_components, style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center',
                                               'marginTop': '70px'})

# Register the page with the Dash app
dash.register_page(__name__, path="/batteries", layout=layout)




# these will be connect to status bar and connect to backend


# Callbacks to update selected port and baudrate
# @app.callback(
#     Output('selected-port', 'data'),
#     Input({'type': 'port-item', 'index': dash.dependencies.ALL}, 'n_clicks'),
#     [State({'type': 'port-item', 'index': dash.dependencies.ALL}, 'children')],
# )


# def update_selected_port(n_clicks, port_labels):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         return dash.no_update
#     else:
#         button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#         selected_index = eval(button_id)['index']
#         return port_labels[selected_index]

# @app.callback(
#     Output('selected-baudrate', 'data'),
#     Input({'type': 'baudrate-item', 'index': dash.dependencies.ALL}, 'n_clicks'),
#     [State({'type': 'baudrate-item', 'index': dash.dependencies.ALL}, 'children')],
# )
# def update_selected_baudrate(n_clicks, baudrate_labels):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         return dash.no_update
#     else:
#         button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#         selected_index = eval(button_id)['index']
#         return baudrate_labels[selected_index]

# Callback to handle serial connection
# @app.callback(
#     Output("connect-button", "n_clicks"),
#     Input("connect-button", "n_clicks"),
#     State('selected-port', 'data'),
#     State('selected-baudrate', 'data'),
# )
# def handle_connect(n_clicks, selected_port, selected_baudrate):
#     if n_clicks > 0 and selected_port and selected_baudrate:
#         try:
#             ser = serial.Serial(selected_port, selected_baudrate)
#             print(f"Connected to {selected_port} at {selected_baudrate} baud rate")
#             # Here you can add additional logic after establishing the connection
#         except Exception as e:
#             print(f"Failed to connect: {e}")
#     return 0  # Reset the click count after handling

