# coding=utf-8

from util.common import DictObj


class ResourceInfo:
    """
    资源信息model. 对应于首页的"更新/热门"资源数据结构
    """
    def __init__(self, title, movie_link="", link="", size="", rating=""):
        self.title = title
        self.movie_link = movie_link
        self.link = link
        self.size = size
        self.rating = rating

    def info(self):
        return DictObj({
            "title": self.title,
            "movie_link": self.movie_link,
            "link": self.link,
            "size": self.size,
            "rating": self.rating,
        })
