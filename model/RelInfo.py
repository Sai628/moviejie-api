# coding=utf-8

from util.common import DictObj


class RelInfo:
    """
    相关电影/电视剧. 对应URL: /movie/<movie_id> 页面中的"相关影视"/"猜你喜欢"数据结构
    """
    def __init__(self, category, resources):
        self.category = category
        self.resources = resources

    def info(self):
        return DictObj({
            "category": self.category,
            "resources": self.resources,
        })
