from dash import Input, Output, State

def register_callbacks(app):
    @app.callback(
        Output("charges-collapse", "is_open"),
        [Input("charges-toggle", "n_clicks")],
        [State("charges-collapse", "is_open")],
    )
    def toggle_charges_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
        Output("actions-collapse", "is_open"),
        [Input("actions-toggle", "n_clicks")],
        [State("actions-collapse", "is_open")],
    )
    def toggle_actions_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
        Output("save-data-collapse", "is_open"),
        [Input("save-data-toggle", "n_clicks")],
        [State("save-data-collapse", "is_open")],
    )
    def toggle_save_data_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    @app.callback(
        Output("reset-errors-link", "active"),
        [Input("reset-errors-link", "n_clicks")],
    )
    def reset_errors(n):
        if n:
            print("Errors reset!")
        return False
