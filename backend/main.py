from flask import Flask, request, render_template
from flask_cors import CORS
from extensions import MANGA_MODULES
from modules.helpers import get_image
import base64

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def index():
   return render_template('index.html', data={
      'sources': [
        { 
          'id': k,
          'name': MANGA_MODULES[k]['name'],
          'description': MANGA_MODULES[k]['description'],
          'url': MANGA_MODULES[k]['referer'],
        }
        for k in MANGA_MODULES
      ]
   })

@app.route("/<int:source>/search/<name>", methods=['GET'])
def search(name: str, source: int):
  m = MANGA_MODULES[source]
  return {
    'source': source,
    'source_url': m['referer'],
    'result': m['module'].search(name)
  }

@app.route("/<int:source>/manga", methods=['GET'])
def manga(source: int):
    args = request.args
    url = args.get('url')

    if not url:
      return { 'error': "You must pass a url of the source!\nExample: /1/manga?url=https://readmangabat.com/read-mx357842"}
    
    m = MANGA_MODULES[source]
    return {
      'source': source,
      'source_url': m['referer'],
      'result': m['module'].get_manga(url)
    }

@app.route("/<int:source>/chapter", methods=['GET'])
def chapter(source: int):
    args = request.args
    url = args.get('url')

    if not url:
      return { 'error': "You must pass a url of the source!\nExample: /1/chapter?url=https://readmangabat.com/read-mx357842"}
    
    m = MANGA_MODULES[source]
    return {
      'source': source,
      'source_url': m['referer'],
      'result': m['module'].get_chapter(url)
    }

@app.route("/get-image", methods=['GET'])
def image():
  args = request.args
  url = args.get('url')
  referer = args.get('referer')

  if not url or not referer:
    return { 'Error': "Url and referer are required!" }
  
  image = get_image(url, referer)
  return "data:image/png;base64," + image

if __name__ == '__main__':
  app.run('0.0.0.0', port=8000)