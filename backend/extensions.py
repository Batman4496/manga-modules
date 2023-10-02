import modules.mangabat as mangabat
import modules.mangatown as mangatown

MANGA_MODULES = {
  1: {
    'name': "MangaBat",
    'description': "Scrapper for mangabat",
    'module': mangabat.MangaBat(),
    'referer': mangabat.REQUEST_URL
  },
  2: {
    'name': "MangaTown",
    'description': "Scrapper for mangatown",
    'module': mangatown.MangaTown(),
    'referer':  mangatown.REQUEST_URL
  }
}