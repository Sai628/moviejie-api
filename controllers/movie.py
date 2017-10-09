# coding=utf-8

from flask_restful import Resource

from util.helper import *
from config import config
from model import MovieInfo, LinkInfo


class Movie(Resource):
    def get(self, movie_id):
        movie_soup = get_html_soup(config.API_DOMAIN + "/movie/" + movie_id)

        # "电影/电视剧"标题
        title = movie_soup.find('div', id='movie_title').text.strip()

        # 基本信息字段
        infos_div = movie_soup.find('div', id='movie_info')
        banner = infos_div.find('img')['src']
        directors = get_info_text(infos_div, 'directors')
        writers = get_info_text(infos_div, 'writers')
        stars = get_info_text(infos_div, 'stars')
        genres = get_info_text(infos_div, 'genres')
        country = get_info_text(infos_div, 'country')
        release_date = get_info_text(infos_div, 'release_date')
        akaname = get_info_text(infos_div, 'akaname')
        star = get_info_text(infos_div, 'star')

        # 下载链接信息列表
        links = []
        for tr in movie_soup.find('tbody').find_all('tr'):
            td_tags = tr.find_all('td')

            name_tag = td_tags[0]
            name = name_tag.text.strip() if name_tag is not None else ''

            size = td_tags[1].text
            dimen = td_tags[2].text
            format = td_tags[3].text

            link_a_tag = td_tags[4].a
            link = link_a_tag['href'] if link_a_tag is not None else ''

            link_info = LinkInfo(name=name, size=size, dimen=dimen, format=format, link=link)
            links.append(link_info.info())

        movie_info = MovieInfo(title=title, banner=banner, directors=directors, writers=writers, stars=stars,
                               genres=genres, country=country, release_date=release_date, akaname=akaname, star=star,
                               links=links)

        return success({
            "movie": movie_info.info()
        })


def get_info_text(tag, class_):
    return tag.find('p', class_=class_).text.split('：')[1].strip()
