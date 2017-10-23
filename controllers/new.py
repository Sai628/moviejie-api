# coding=utf-8

from flask_restful import Resource

from app import cache
from config import config
from model import MovieSimpleInfo, OSTSimpleInfo
from util.helper import *


class NewMovie(Resource):
    @cache.memoize(timeout=config.CACHE_EXPIRE_TIME)
    def get(self, page):
        movies = get_movie_simple_infos(config.API_NEW_MOVIE + page)
        return success({
            "movies": movies
        })

    def __repr__(self):
        return "%s" % self.__class__.__name__


class NewTv(Resource):
    @cache.memoize(timeout=config.CACHE_EXPIRE_TIME)
    def get(self, page):
        movies = get_movie_simple_infos(config.API_NEW_TV + page)
        return success({
            "movies": movies
        })

    def __repr__(self):
        return "%s" % self.__class__.__name__


class NewOST(Resource):
    @cache.memoize(timeout=config.CACHE_EXPIRE_TIME)
    def get(self, page):
        ost_soup = get_html_soup(config.API_NEW_OST + page)
        search_result_div = ost_soup.find('div', id='search_result')
        ul_tag = search_result_div.find('ul')

        ost_simple_infos = []
        for li_tag in ul_tag.find_all('li'):
            # 标题
            title_tag = li_tag.find('p', class_='movie_name')
            movie_name = title_tag.text.strip() if title_tag is not None else ''

            # 电影详情页面链接
            movie_link = title_tag.a['href'] if title_tag.a is not None else ''

            # 封面图片
            banner_img_tag = li_tag.find('img', class_='banner')
            banner = banner_img_tag['src'] if banner_img_tag is not None else ''

            res_name = get_p_text(li_tag, 'res_name')  # 资源名称
            res_size = get_p_text(li_tag, 'res_size')  # 资源大小
            country = get_span_text(li_tag, 'country')  # 地区/语言
            publish_time = get_span_text(li_tag, 'time')  # 发行时间
            file_type = get_span_text(li_tag, 'filetype')  # 资源格式
            ost_simple_info = OSTSimpleInfo(movie_name=movie_name, movie_link=movie_link, banner=banner,
                                            res_name=res_name, res_size=res_size, country=country,
                                            publish_time=publish_time, file_type=file_type)
            ost_simple_infos.append(ost_simple_info.info())
        return success({
            "ost_infos": ost_simple_infos
        })

    def __repr__(self):
        return "%s" % self.__class__.__name__


def get_movie_simple_infos(url):
    movie_soup = get_html_soup(url)
    search_result_div = movie_soup.find('div', id='search_result')
    ul_tag = search_result_div.find('ul')

    movie_simple_infos = []
    for li_tag in ul_tag.find_all('li'):
        # 标题
        title_tag = li_tag.find('a', class_='name')
        title = title_tag.text.strip() if title_tag is not None else ''
        movie_link = title_tag['href'] if title_tag is not None else ''

        # 封面图片
        banner_img_tag = li_tag.find('img', class_='banner')
        banner = banner_img_tag['src'] if banner_img_tag is not None else ''

        genres = get_span_text(li_tag, 'genres')  # 类型
        country = get_span_text(li_tag, 'country')  # 国家/地区
        star = get_span_text(li_tag, 'star')  # 评分
        movie_simple_info = MovieSimpleInfo(title=title, movie_link=movie_link, banner=banner, genres=genres,
                                            country=country, star=star)
        movie_simple_infos.append(movie_simple_info.info())
    return movie_simple_infos


