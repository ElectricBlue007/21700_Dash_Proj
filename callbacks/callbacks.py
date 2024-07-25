from dash import Input, Output, State
import dash

app = dash.Dash(__name__)


def register_callbacks(app):
    @app.callback(
        Output("charges-collapse", "is_open"),
        Output("actions-collapse", "is_open"),
        Output("save-data-collapse", "is_open"),
        Output("operation-collapse", "is_open"),
        Input("charges-toggle", "n_clicks"),
        Input("actions-toggle", "n_clicks"),
        Input("save-data-toggle", "n_clicks"),
        Input("operation-toggle", "n_clicks"),
        State("charges-collapse", "is_open"),
        State("actions-collapse", "is_open"),
        State("save-data-collapse", "is_open"),
        State("operation-collapse", "is_open"),
    )
    def toggle_collapse(charges_n, actions_n, save_data_n, operation_n,
                        charges_is_open, actions_is_open, save_data_is_open, operation_is_open):
        ctx = dash.callback_context

        if not ctx.triggered:
            return charges_is_open, actions_is_open, save_data_is_open, operation_is_open

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == "charges-toggle":
            return not charges_is_open, False, False, False
        elif button_id == "actions-toggle":
            return False, not actions_is_open, False, False
        elif button_id == "save-data-toggle":
            return False, False, not save_data_is_open, False
        elif button_id == "operation-toggle":
            return False, False, False, not operation_is_open

        return charges_is_open, actions_is_open, save_data_is_open, operation_is_open

    @app.callback(
        Output("reset-errors-link", "active"),
        [Input("reset-errors-link", "n_clicks")],
    )
    def reset_errors(n):
        if n:
            print("Errors reset!")
        return False
