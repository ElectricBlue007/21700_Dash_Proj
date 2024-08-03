import dash
import dash_bootstrap_components as dbc
from dash import html, page_container
from callbacks.callbacks import register_callbacks, register_selector_callbacks
from layouts.sidebar import sidebar

app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MATERIA, dbc.icons.FONT_AWESOME],
    assets_folder='assets'
)

# Define the layout with dynamic margins
app.layout = html.Div(
    [
        sidebar,
        html.Div(
            [
                page_container
            ],
            id='page-content',
            className="content",
            style={
                # 'marginLeft': '320px',
                # 'marginTop': '70px',
                # 'padding': '-10px'
            }
        ),
    ]
)

# Register callbacks
register_callbacks(app)
register_selector_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
