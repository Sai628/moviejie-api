# coding=utf-8

from flask_restful import Resource

from app import cache
from config import config
from model import OSTInfo, LinkInfo
from util.helper import *


class OST(Resource):
    @cache.memoize(timeout=config.CACHE_EXPIRE_TIME)
    def get(self, ost_id):
        ost_soup = get_html_soup(config.API_DOMAIN + "/ost/" + ost_id)

        # "电影/电视剧"标题
        title_div = ost_soup.find('div', id='ost_title')
        if title_div is not None:
            movie_name = title_div.a.text.strip() if title_div.a is not None else ''
            movie_link = title_div.a['href'] if title_div.a is not None else ''

        # 基本信息字段
        banner = ost_soup.find('img', class_='ost_cover')['src']
        res_name = get_tag_child_text(tag=ost_soup, child_tag_name='h2', class_name='res_title')
        country = get_span_text(ost_soup, 'country')
        language = get_span_text(ost_soup, 'language')
        publish_time = get_span_text(ost_soup, 'time')
        file_type = get_span_text(ost_soup, 'filetype')

        # 专辑曲目列表
        track_list = []
        track_tag = ost_soup.find('p', class_='inner_content')
        if track_tag is not None:
            # 去除曲目 html 中的 "<!--Wrap-head end-->" 与 "<!--Wrap-tail begin-->" 字符, 以及 "<br>" 标签
            tracks = filter(lambda x: x not in ['\n', 'Wrap-tail begin', 'Wrap-head end'] and str(x) != '<br/>',
                            track_tag.contents)
            track_list = ["".join(str(track).split('.')[1:]).strip() for track in tracks]  # 去除曲目前面的序号
            print track_list

        # 专辑曲目下载链接信息列表
        link_infos = []
        for tr in ost_soup.find('table').find_all('tr'):
            name_tag = tr.find('td', class_='movie_name')
            if name_tag is None:
                continue

            td_tags = tr.find_all('td')
            name = td_tags[0].text.strip()
            size = td_tags[1].text.strip()
            link = td_tags[2].a['href'] if td_tags[2].a is not None else ''

            link_info = LinkInfo(name=name, size=size, link=link)
            link_infos.append(link_info.info())

        ost_info = OSTInfo(movie_name=movie_name, movie_link=movie_link, banner=banner, res_name=res_name,
                           country=country, language=language, publish_time=publish_time, file_type=file_type,
                           track_list=track_list, links=link_infos)
        return success({
            "ost": ost_info.info()
        })

    def __repr__(self):
        return "%s" % self.__class__.__name__
