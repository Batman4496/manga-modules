import requests
from modules.mangabat import MangaBat
from modules.mangatown import MangaTown

def get_image(url: str):
  res = requests.get(url, headers={
    'referer': "https://readmangabat.com/"
  })
  
  return res


if __name__ == '__main__':
  manga = MangaTown()
  search = manga.search('teenage')
  details = manga.get_manga(search[0].get('url'))
  chapter = manga.get_chapter(details['chapters'][0]['url'])
  print(chapter[0])
  image = get_image('https://v15.mkklcdnv6tempv5.com/img/tab_35/03/58/25/jz987182/chapter_145/1-f.jpg')

  # manga = MangaBat()
  # search = manga.search('teenage')
  # details = manga.get_manga(search[0].get('url'))
  # chapter = manga.get_chapter(details['chapters'][0]['url'])
