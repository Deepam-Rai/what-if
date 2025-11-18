from pyramid.renderers import render
from pyramid.url import route_path
from pyramid.view import view_config
from .story_engine import STORY


@view_config(
    route_name="home",
    renderer="templates/scene.mako"
)
def home(request):
    return {"node": STORY["start"], "request": request}


@view_config(
    route_name="scene",
    renderer="templates/scene.mako"
)
def scene(request):
    node_id = request.matchdict["node"]
    node = STORY.get(node_id)

    if not node:
        node = {
            "title": "Timeline Lost",
            "text": "This timeline branch does not exist.",
            "choices": [{"text": "Return to Start", "to": "start"}]
        }
    
    return {"node": node, "request": request}