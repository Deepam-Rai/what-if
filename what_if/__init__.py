from pyramid.config import Configurator
from waitress import serve


def main(global_config=None, **settings):
    """
    This function returns a Pyramid WSGI application.
    uv will call this function when running the app.
    """
    # Create config object
    config = Configurator(settings=settings)

    # Enable mako templates
    config.include("pyramid_mako")

    # Include routes from routes.py
    config.include(".routes")

    # Scan for @view_config decorated views
    config.scan(".views")

    # Create the WSGI app
    return config.make_wsgi_app()


def run():
    # Start the server directly when using uv run what-if
    app = main()
    print("Serving at http://127.0.0.1:6543")
    serve(app, host="127.0.0.1", port=6543)
