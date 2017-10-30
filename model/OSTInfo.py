# coding=utf-8

from util.common import DictObj


class OSTInfo:
    """
    原声大碟信息model. 对应URL: /ost/<ost_id>/ 页面中的数据结构
    """
    def __init__(self, movie_name=None, movie_link=None, banner=None, res_name=None, country=None,
                 language=None, publish_time=None, file_type=None, track_list=None, links=None):
        self.movie_name = movie_name  # 电影名称
        self.movie_link = movie_link  # 电影详情页面链接
        self.banner = banner  # 封面图URL
        self.res_name = res_name  # 资源名称
        self.country = country  # 地区
        self.language = language  # 语言
        self.publish_time = publish_time  # 发行时间
        self.file_type = file_type  # 资源格式
        self.track_list = track_list  # 专辑曲目列表. 数据类型: [string]
        self.links = links  # 下载页面链接列表

    def info(self):
        return DictObj({
            "movie_name": self.movie_name,
            "movie_link": self.movie_link,
            "banner": self.banner,
            "res_name": self.res_name,
            "country": self.country,
            "language": self.language,
            "publish_time": self.publish_time,
            "file_type": self.file_type,
            "track_list": self.track_list,
            "links": self.links,
        })
