# coding=utf-8

from flask_restful import Resource

from app import cache
from util.helper import *
from config import config
from model import MovieSimpleInfo


class NewMovie(Resource):
    @cache.memoize(timeout=config.CACHE_EXPIRE_TIME)
    def get(self, page):
        movie_soup = get_html_soup(config.API_NEW_MOVIE + page)

        search_result_div = movie_soup.find('div', id='search_result')
        ul_tag = search_result_div.find('ul')

        movie_simple_infos = []
        for li_tag in ul_tag.find_all('li'):
            # 标题
            title_tag = li_tag.find('a', class_='name')
            title = title_tag.text.strip() if title_tag is not None else ''
            movie_link = title_tag['href'] if title_tag is not  None else ''

            # 封面图片
            banner_img_tag = li_tag.find('img', class_='banner')
            banner = banner_img_tag['src'] if banner_img_tag is not None else ''

            genres = get_span_text(li_tag, 'genres')  # 类型
            country = get_span_text(li_tag, 'country')  # 国家/地区
            star = get_span_text(li_tag, 'star')  # 评分
            movie_simple_info = MovieSimpleInfo(title=title, movie_link=movie_link, banner=banner, genres=genres,
                                                country=country, star=star)
            movie_simple_infos.append(movie_simple_info.info())

        return success({
            "movies": movie_simple_infos
        })

    def __repr__(self):
        return "%s" % self.__class__.__name__


def get_span_text(tag, class_name):
    span_tag = tag.find('span', class_=class_name)
    return span_tag.text.split('：')[1].strip() if span_tag is not None else ''