# Code to fetch the Jupyter Notebook file from GitHub and convert to HTML
import requests
import json
import base64
import nbformat
from nbconvert import HTMLExporter


def get_notebook_content():
    url = 'https://api.github.com/repos/jeanruggiero/mission-compostable/contents/com-python/image_processing_engine' \
          '.ipynb'
    content = requests.get(url).content

    notebook_content = base64.b64decode(json.loads(content.decode()).get('content')).decode()
    notebook = nbformat.reads(notebook_content, as_version=4)

    exporter = HTMLExporter()
    (body, resources) = exporter.from_notebook_node(notebook)

    return body

