import requests
from bs4 import BeautifulSoup
from modules.helpers import extract_data

REQUEST_URL = "https://readmangabat.com"

class MangaBat:

  def search(self, search_keyword: str) -> list[dict]:
    res = requests.post(f"{REQUEST_URL}/getstorysearchjson", { 
      'searchword': search_keyword
    })

    return extract_data(
      res.json().get('searchlist'),
      keys={
        'title': 'name',
        'url': 'url_story'
      }
    )

  def get_chapters_list(self, url: str) -> list[dict]:
    data = []
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    chapters = soup.find_all('a', { 'class': 'chapter-name' })

    for index, chapter in enumerate(chapters[::-1]):
      data.append({
        'chapter': index + 1,
        'title': chapter.text,
        'url': chapter.get('href')
      })
    
    return data

  def get_manga(self, url: str) -> dict:
    data = {}
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    left = soup.find('div', { 'class': 'story-info-left' })
    right = soup.find('div', { 'class': 'story-info-right' })
    data['image'] = left.find('img').get('src')
    data['title'] = right.find('h1').text
    data['description'] = soup.find('div', { 'id': 'panel-story-info-description' }).text

    table = right.find('table', { 'class': 'variations-tableInfo' })
    table_rows = table.find_all('tr')

    for row in table_rows:
      splitted = row.text.split()
      if len(splitted) < 3:
        continue

      if 'status' in splitted[0].lower():
        data['status'] = splitted[2]
         
      if 'alt' in splitted[0].lower():
        data['alt'] = ''.join(splitted[2:])
      
      if 'genre' in splitted[0].lower():
        data['genres'] = ''.join(splitted[2:])
      
      if 'author' in splitted[0].lower():
        data['author'] = ''.join(splitted[2:])

    chapters = self.get_chapters_list(url)
    data['chapters'] = chapters
    
    return data

  def get_chapter(self, url: str) -> list[dict]:
    data = []
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    container = soup.find('div', { 'class': 'container-chapter-reader' })
    images = container.find_all('img', { 'class': 'img-content' })
    
    for index, image in enumerate(images):
      data.append({
        'page': index,
        'name': image.get('alt'),
        'image': image.get('src') 
      })

    return data