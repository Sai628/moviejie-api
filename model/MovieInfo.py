# coding=utf-8

from util.common import DictObj


class MovieInfo:
    """
    电影/电视剧信息model. 对应URL: /movie/<movie_id> 页面中的数据结构
    """
    def __init__(self, title=None, banner=None, directors=None, writers=None, stars=None,
                 genres=None, country=None, release_date=None, akaname=None, star=None,
                 links=None):
        self.title = title
        self.banner = banner
        self.directors = directors
        self.writers = writers
        self.stars = stars
        self.genres = genres
        self.country = country
        self.release_date = release_date
        self.akaname = akaname
        self.star = star
        self.links = links

    def info(self):
        return DictObj({
            "title": self.title,
            "banner": self.banner,
            "directors": self.directors,
            "writers": self.writers,
            "stars": self.stars,
            "genres": self.genres,
            "country": self.country,
            "release_date": self.release_date,
            "akaname": self.akaname,
            "star": self.star,
            "links": self.links
        })
