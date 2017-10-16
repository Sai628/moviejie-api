# coding=utf-8

from util.common import DictObj


class LinkDetailInfo:
    """
    下载链接详情信息model. 对应URL: /link/<link_id>/ 页面中的数据结构
    """
    def __init__(self, movie_title=None, movie_link=None, name=None, size=None, download_link=None):
        self.movie_title = movie_title
        self.movie_link = movie_link
        self.name = name
        self.size = size
        self.download_link = download_link

    def info(self):
        return DictObj({
            "movie_title": self.movie_title,
            "movie_link": self.movie_link,
            "name": self.name,
            "size": self.size,
            "download_link": self.download_link
        })
