# coding=utf-8

from util.common import DictObj


class LinkInfo:
    """
    下载链接信息model. 对应URL: /movie/<movie_id> 页面中下载链接列表每项的数据结构
    """
    def __init__(self, name=None, size=None, dimen=None, format=None, link=None):
        self.name = name
        self.size = size
        self.dimen = dimen
        self.format = format
        self.link = link

    def info(self):
        return DictObj({
            "name": self.name,
            "size": self.size,
            "dimen": self.dimen,
            "format": self.format,
            "link": self.link
        })
