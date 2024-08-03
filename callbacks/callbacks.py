from dash import Input, Output, State
import dash

app = dash.Dash(__name__)

def register_callbacks(app):

    @app.callback(
        Output("reset-errors-link", "active"),
        [Input("reset-errors-link", "n_clicks")],
    )
    def reset_errors(n):
        if n:
            print("Errors reset!")
        return False
