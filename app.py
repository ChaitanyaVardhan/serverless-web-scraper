from chalice import Chalice, Response
import os
import jinja2
import json

app = Chalice(app_name="web-scraper-v1")


def render(tpl_path=None, context=None):
    path, filename = os.path.split(tpl_path)
    if context:
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(path or "./")).get_template(
                filename
            ).render(context)
    else:
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(path or "./")).get_template(
                filename
            ).render()


@app.route('/')
def index():
    template = render(
        tpl_path='chalicelib/templates/index.html'
    )
    return Response(json.loads(template))
    
