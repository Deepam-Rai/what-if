from pyramid.config import Configurator

def includeme(config: Configurator):
    config.add_route("home", "/")
    config.add_route("scene", "/scene/{node}")
