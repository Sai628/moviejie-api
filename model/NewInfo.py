# coding=utf-8

from util.common import DictObj


class NewInfo:
    """
    更新信息model. 对应于首页中的更新列表
    """
    def __init__(self, category, resources):
        self.category = category
        self.resources = resources

    def info(self):
        return DictObj({
            "category": self.category,
            "resources": self.resources,
        })
