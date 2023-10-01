
# Manga Modules

A small package for scarping mangas from different sources. Using 
`Flask`, `BeautifulSoup`, `requests` library.


## Roadmap

- More extension supports (maybe)

- More features (maybe)

- Web, Desktop, Mobile app (maybe)


## Contributing

HO! You want to contribute?!

Well, make sure you follow the existing code structure or else EVERYTHIN will break.

### Modules

Each module is located in `/modules` dir, make sure to follow the structure of previous modules.

- Have a global var `REQUEST_URL` for the root url of the website.
- Follow the below interface for making functions:

`def search(self, search_keyword: str) -> list[dict]`: For searching mangas

`def get_manga(self, url: str) -> dict`: For getting manga details

`def get_chapter(self, url: str) -> list[dict]`: For getting a specific chapter of manga, this gives the link to pages of chapter as well.

Don't forget to register your modules in `extensions.py` after you are done making one. You may code however you like and also improve the code while you are at it ✌️✌️