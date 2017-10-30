# coding=utf-8

from util.common import DictObj


class OSTSimpleInfo:
    """
    原声大碟简略信息model. 对应URL: /new/ost/ 页面中的数据结构
    """
    def __init__(self, movie_name=None, ost_link=None, banner=None, res_name=None,
                 res_size=None, country=None, publish_time=None, file_type=None):
        self.movie_name = movie_name  # 电影名称
        self.ost_link = ost_link  # 原声大碟详情页面链接
        self.banner = banner  # 封面图URL
        self.res_name = res_name  # 资源名称
        self.res_size = res_size  # 资源大小
        self.country = country  # 地区/语言
        self.publish_time = publish_time  # 发行时间
        self.file_type = file_type  # 资源格式

    def info(self):
        return DictObj({
            "movie_name": self.movie_name,
            "ost_link": self.ost_link,
            "banner": self.banner,
            "res_name": self.res_name,
            "res_size": self.res_size,
            "country": self.country,
            "publish_time": self.publish_time,
            "file_type": self.file_type,
        })
