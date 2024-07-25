import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML

app = dash.Dash(__name__)

# Define the HTML template for the battery component
battery_html_template = '''
<section class="battery">
    <div class="battery__card">
        <div class="battery__data">
            <h1 class="battery__percentage">{percentage}%</h1>
            <p class="battery__status">{status}</p>
        </div>
        <div class="battery__pill">
            <div class="battery__level">
                <div class="battery__liquid" style="height: {liquid_height}%; background: {liquid_color};"></div>
            </div>
        </div>
    </div>
</section>
'''

# Initialize the battery data for 90 batteries
battery_data = [{'percentage': 20, 'status': 'Low battery', 'liquid_color': 'linear-gradient(90deg, hsl(7, 89%, 46%) 15%, hsl(11, 93%, 68%) 100%)'} for _ in range(90)]


# Function to determine battery status and color
def get_battery_status_and_color(percentage):
    if percentage <= 20:
        return "Low battery", 'linear-gradient(90deg, hsl(7, 89%, 46%) 15%, hsl(11, 93%, 68%) 100%)'
    elif percentage <= 40:
        return "", 'linear-gradient(90deg, hsl(22, 89%, 46%) 15%, hsl(54, 90%, 45%) 100%)'
    elif percentage <= 80:
        return "", 'linear-gradient(90deg, hsl(54, 89%, 46%) 15%, hsl(92, 90%, 45%) 100%)'
    else:
        return "Full battery", 'linear-gradient(90deg, hsl(92, 89%, 46%) 15%, hsl(92, 90%, 68%) 100%)'


# Define the layout of the Dash app
app.layout = html.Div([
    html.Div(id='battery-components', style={'display': 'flex', 'flexWrap': 'wrap'}),
    dcc.Dropdown(
        id='battery-selector',
        options=[{'label': f'Battery {i}', 'value': i} for i in range(1, 91)],
        placeholder='Select a battery to update',
        style={'margin': '10px', 'backgroundColor': 'white', 'color': 'black'}
    ),
    dcc.Input(id='battery-input', type='number', min=0, max=100, step=1, value=20, style={'margin-right': '10px'}),
    html.Button('Update Battery', id='update-button', n_clicks=0)
])


# Callback to update the battery components
@app.callback(
    Output('battery-components', 'children'),
    Input('update-button', 'n_clicks'),
    [State('battery-selector', 'value'), State('battery-input', 'value')]
)
def update_battery_components(n_clicks, selected_battery, battery_percentage):
    if selected_battery is not None and battery_percentage is not None:
        # Update the selected battery data
        status, color = get_battery_status_and_color(battery_percentage)
        battery_data[selected_battery - 1] = {'percentage': battery_percentage, 'status': status, 'liquid_color': color}

    # Generate the battery components
    battery_components = []
    for row in range(9):
        row_components = []
        for col in range(10):
            index = row * 10 + col
            battery = battery_data[index]
            battery_html = battery_html_template.format(
                percentage=battery['percentage'],
                status=battery['status'],
                liquid_height=battery['percentage'],
                liquid_color=battery['liquid_color']
            )
            row_components.append(html.Div(DangerouslySetInnerHTML(battery_html), style={'margin': '5px'}))
        battery_components.append(html.Div(row_components, style={'display': 'flex'}))
    return battery_components


if __name__ == '__main__':
    app.run_server(debug=True)
