# coding=utf-8

from util.common import DictObj


class MovieInfo:
    """
    电影/电视剧信息model. 对应URL: /movie/<movie_id>/ 页面中的数据结构
    """
    def __init__(self, title=None, banner=None, directors=None, writers=None, stars=None, genres=None,
                 country=None, release_date=None, runtime=None, akaname=None, star=None,  story=None,
                 links=None, related_resources=None, recommended_resources=None):
        self.title = title  # 标题
        self.banner = banner  # 封面图URL
        self.directors = directors  # 导演
        self.writers = writers  # 编剧
        self.stars = stars  # 主演
        self.genres = genres  # 类型
        self.country = country  # 国家/地区
        self.release_date = release_date  # 上映日期
        self.runtime = runtime  # 片长
        self.akaname = akaname  # 又名
        self.star = star  # 评分
        self.story = story  # 剧情简介
        self.links = links  # 下载页面链接列表
        self.related_resources = related_resources  # 相关资源列表
        self.recommended_resources = recommended_resources  # 推荐资源列表

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
            "runtime": self.runtime,
            "akaname": self.akaname,
            "star": self.star,
            "story": self.story,
            "links": self.links,
            "related_resources": self.related_resources,
            "recommended_resources": self.recommended_resources,
        })
