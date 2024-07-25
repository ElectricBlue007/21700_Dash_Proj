import dash_table
from dash import Dash, dash_table

app = Dash(__name__)
# app.layout = html.Div([
#     dcc.Dropdown(["All Process Step Data"], 'All Process Step Data', id='Process Steps')])
# app.layout = html.Div([
#     dcc.Dropdown(["All", "End"], 'All', id='Step Type')])
# app.layout = html.Div([
#     dcc.Dropdown(["Process 1", "Process 2"], id="Process")])
# table

app.layout = dash_table.DataTable([{"name": "hi", "id": "hello"}])

if __name__ == '__main__':
    app.run(debug=True)
