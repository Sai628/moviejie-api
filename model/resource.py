# coding=utf-8

from util.common import DictObj


class ResourceInfo:
    def __init__(self, title, size, movie_link, link):
        self.title = title
        self.size = size
        self.movie_link = movie_link
        self.link = link

    def info(self):
        return DictObj({
            "title": self.title,
            "size": self.size,
            "movie_link": self.movie_link,
            "link": self.link,
        })
