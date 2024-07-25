import dash
import dash_bootstrap_components as dbc
from dash import html, page_container
from callbacks.callbacks import register_callbacks
from layouts.sidebar import sidebar
from layouts.navbar import navbar

# Initialize the Dash app
app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MATERIA, dbc.icons.FONT_AWESOME],
)

# Define the layout of the app
app.layout = html.Div(
    [
        sidebar,  # Sidebar layout
        navbar,  # Navbar layout
        html.Div(
            [
                page_container
            ],
            className="content",
            style={
                'marginLeft': '228px',
                'marginTop': '70px',
                'padding': '20px'
            }
        ),
    ]
)

# Register callbacks
register_callbacks(app)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
