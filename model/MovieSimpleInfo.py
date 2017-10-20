# coding=utf-8

from util.common import DictObj


class MovieSimpleInfo:
    """
    电影/电视剧简略信息model. 对应URL: /new/movie/ 与 /new/tv/ 页面中的数据结构
    """
    def __init__(self, title=None, movie_link=None, banner=None, genres=None, country=None, star=None):
        self.title = title  # 标题
        self.movie_link = movie_link  # 电影详情页面链接
        self.banner = banner  # 封面图URL
        self.genres = genres  # 类型
        self.country = country  # 国家/地区
        self.star = star  # 评分

    def info(self):
        return DictObj({
            "title": self.title,
            "movie_link": self.movie_link,
            "banner": self.banner,
            "genres": self.genres,
            "country": self.country,
            "star": self.star,
        })
