# coding=utf-8

from util.common import DictObj


class IndexInfo:
    def __init__(self, category, resources):
        self.category = category
        self.resources = resources

    def info(self):
        return DictObj({
            "category": self.category,
            "resources": self.resources,
        })
