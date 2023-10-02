from flask import Flask, request, render_template
from extensions import MANGA_MODULES
from modules.helpers import get_image

app = Flask(__name__)

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
    'source': m['referer'],
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
      'source': m['referer'],
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
      'source': m['referer'],
      'result': m['module'].get_chapter(url)
    }

# @app.route("/<int:source>/page", methods=['GET'])
# def page(source: int):
#   args = request.args
#   url = args.get('url')

#   if not url:
#     return { 'error': "You must pass a url of the source!\nExample: /1/page?url=https://zjcdn.mangahere.org/store/manga/13517/001.0/compressed/j003.jpg"}
  
#   page = get_image(url, MANGA_MODULES[source]['referer'])
#   return page

if __name__ == '__main__':
  app.run('0.0.0.0', port=8000)