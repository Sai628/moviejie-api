# coding=utf-8

from util.common import DictObj


class HotInfo:
    """
    热门信息model. 对应于首页中的热门剧集/电影
    """
    def __init__(self, category, resources):
        self.category = category
        self.resources = resources

    def info(self):
        return DictObj({
            "category": self.category,
            "resources": self.resources,
        })
