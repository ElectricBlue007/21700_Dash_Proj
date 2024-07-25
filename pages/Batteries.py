import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
import serial
from layouts.Navbar import navbar2

app = dash.Dash(__name__)

battery_html_template = '''
<section class="battery">
    <div class="battery__card glass" style="width: 130px; height: 150px; border: 1px solid rgba(82, 63, 233, 0.60); position: relative;">
        <div class="battery__data">
            <h1 class="battery__percentage" style="font-size: 20px; margin-bottom: 5px; line-height: 1;">{percentage}%</h1>
            <p class="battery__status" style="font-size: 15px; margin-bottom: 3px; line-height: 1;">{status}</p>
            <p class="battery__extra" style="font-size: 15px; margin-bottom: 3px; line-height: 1;">V: {V}</p>
            <p class="battery__extra" style="font-size: 15px; margin-bottom: 3px; line-height: 1;">I: {I}</p>
            <p class="battery__extra" style="font-size: 15px; margin-bottom: 3px; line-height: 1;">C: {C}</p>
            <p class="battery__extra" style="font-size: 15px; margin-bottom: 3px; line-height: 1;">T: {T}</p>
        </div>
        <div class="battery__pill">
            <div class="battery__level">
                <div class="battery__liquid" style="height: {liquid_height}%; background: {liquid_color};"></div>
            </div>
        </div>
        <div class="battery__num" style="position: absolute; bottom: 5px; right: 5px; font-size: 12px; font-weight: bold;">{num}</div>
    </div>
</section>
'''

# Initial battery data
battery_data = [
    {'percentage': 20, 'status': '', 'liquid_color': 'linear-gradient(90deg, hsl(7, 89%, 46%) 15%, hsl(11, 93%, 68%) 100%)',
     'num': i + 1, 'V': 0, 'I': 0, 'C': 0, 'T': 0} for i in range(90)
]


def get_battery_status_and_color(percentage):
    if percentage <= 20:
        return "", 'linear-gradient(90deg, hsl(7, 89%, 46%) 15%, hsl(11, 93%, 68%) 100%)'
    elif percentage <= 40:
        return "", 'linear-gradient(90deg, hsl(22, 89%, 46%) 15%, hsl(54, 90%, 45%) 100%)'
    elif percentage <= 80:
        return "", 'linear-gradient(90deg, hsl(54, 89%, 46%) 15%, hsl(92, 90%, 45%) 100%)'
    else:
        return "", 'linear-gradient(90deg, hsl(92, 89%, 46%) 15%, hsl(92, 90%, 68%) 100%)'


layout = html.Div(id='page-content', className="content", style={
    'marginLeft': '200px',
    'marginTop': '-20px',
    'padding': '20px',
    'background': 'linear-gradient(356deg, rgba(0,0,0,1) 0%, rgba(6,1,61,1) 57%, rgba(0,0,0,1) 100%), rgb(0,0,0)'
},
    children=[
    navbar2,
    html.Div(id='battery-components'),
    dcc.Dropdown(
        id='battery-selector',
        options=[{'label': f'Battery {i}', 'value': i} for i in range(1, 91)],
        placeholder='Select a battery to update',
        style={'margin': '10px', 'backgroundColor': 'white', 'color': 'black'}
    ),
    dcc.Input(id='battery-input', type='number', min=0, max=100, step=1, value=20, style={'margin-right': '10px'}),
    dcc.Input(id='V-input', type='number', placeholder='V', style={'margin-right': '10px'}),
    dcc.Input(id='I-input', type='number', placeholder='I', style={'margin-right': '10px'}),
    dcc.Input(id='C-input', type='number', placeholder='C', style={'margin-right': '10px'}),
    dcc.Input(id='T-input', type='number', placeholder='T', style={'margin-right': '10px'}),
    html.Button('Update Battery', id='update-button', n_clicks=0)
])


@dash.callback(
    Output('battery-components', 'children'),
    Input('update-button', 'n_clicks'),
    [State('battery-selector', 'value'),
     State('battery-input', 'value'),
     State('V-input', 'value'),
     State('I-input', 'value'),
     State('C-input', 'value'),
     State('T-input', 'value')]
)
def update_battery_components(n_clicks, selected_battery, battery_percentage, V, I, C, T):
    if selected_battery is not None and battery_percentage is not None:
        status, color = get_battery_status_and_color(battery_percentage)
        battery_data[selected_battery - 1] = {
            'percentage': battery_percentage,
            'status': status,
            'liquid_color': color,
            'num': selected_battery,
            'V': V,
            'I': I,
            'C': C,
            'T': T
        }

    battery_components = []
    for row in range(10):
        row_components = []
        for col in range(9):
            index = row * 9 + col
            battery = battery_data[index]
            battery_html = battery_html_template.format(
                percentage=battery['percentage'],
                status=battery['status'],
                liquid_height=battery['percentage'],
                liquid_color=battery['liquid_color'],
                num=battery['num'],
                V=battery['V'],
                I=battery['I'],
                C=battery['C'],
                T=battery['T'],
                hue=(battery['num'] * 4) % 360
            )
            row_components.append(html.Div(DangerouslySetInnerHTML(battery_html), style={'marginLeft': '-5px',
                                                                                         'marginTop': '50px',
                                                                                         'padding': '-100px'}))

        battery_components.append(html.Div(row_components, style={'display': 'flex', 'margin-bottom': '-90px'}))
    return battery_components


dash.register_page(__name__, path="/batteries", layout=layout)


@app.callback(
    Output('selected-port', 'data'),
    Input({'type': 'port-item', 'index': dash.dependencies.ALL}, 'n_clicks'),
    [State({'type': 'port-item', 'index': dash.dependencies.ALL}, 'children')],
)
def update_selected_port(n_clicks, port_labels):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        selected_index = eval(button_id)['index']
        return port_labels[selected_index]


@app.callback(
    Output('selected-baudrate', 'data'),
    Input({'type': 'baudrate-item', 'index': dash.dependencies.ALL}, 'n_clicks'),
    [State({'type': 'baudrate-item', 'index': dash.dependencies.ALL}, 'children')],
)


def update_selected_baudrate(n_clicks, baudrate_labels):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        selected_index = eval(button_id)['index']
        return baudrate_labels[selected_index]


@app.callback(
    Output("connect-button", "n_clicks"),
    Input("connect-button", "n_clicks"),
    State('selected-port', 'data'),
    State('selected-baudrate', 'data'),
)
def handle_connect(n_clicks, selected_port, selected_baudrate):
    if n_clicks > 0 and selected_port and selected_baudrate:
        try:
            ser = serial.Serial(selected_port, selected_baudrate)
            print(f"Connected to {selected_port} at {selected_baudrate} baud rate")
            # Here you can add additional logic after establishing the connection
        except Exception as e:
            print(f"Failed to connect: {e}")
    return 0  # Reset the click count after handling


if __name__ == '__main__':
    app.run_server(debug=True)
