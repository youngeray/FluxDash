import dash
from dash import html

def create_dash_app(requests_pathname_prefix: str = None) -> dash.Dash:
    app = dash.Dash(__name__, use_pages=True, requests_pathname_prefix=requests_pathname_prefix)

    app.layout = html.Div([
        dash.page_container
    ])


    return app