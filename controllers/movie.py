# coding=utf-8

from app import cache
from config import config
from flask_restful import Resource
from model import MovieInfo, LinkInfo, ResourceInfo
from util.helper import *
from util.helper import get_p_text


class Movie(Resource):
    @cache.memoize(timeout=config.CACHE_EXPIRE_TIME)
    def get(self, movie_id):
        movie_soup = get_html_soup(config.API_DOMAIN + "/movie/" + movie_id)

        # "电影/电视剧"标题
        title = movie_soup.find('div', id='movie_title').text.strip()

        # 基本信息字段
        infos_div = movie_soup.find('div', id='movie_info')
        banner = infos_div.find('img')['src']
        directors = get_p_text(infos_div, 'directors')
        writers = get_p_text(infos_div, 'writers')
        stars = get_p_text(infos_div, 'stars')
        genres = get_p_text(infos_div, 'genres')
        country = get_p_text(infos_div, 'country')
        release_date = get_p_text(infos_div, 'release_date')
        runtime = get_p_text(infos_div, 'runtime')
        akaname = get_p_text(infos_div, 'akaname')
        star = get_p_text(infos_div, 'star')

        # 下载链接信息列表
        link_infos = []
        for tr in movie_soup.find('tbody').find_all('tr'):
            name_tag = tr.find('td', class_='movie_name')
            if name_tag is None:
                continue

            td_tags = tr.find_all('td')
            name = td_tags[0].text.strip()
            size = td_tags[1].text.strip()
            dimen = td_tags[2].text.strip()
            format = td_tags[3].text.strip()
            link = td_tags[4].a['href'] if td_tags[4].a is not None else ''

            link_info = LinkInfo(name=name, size=size, dimen=dimen, format=format, link=link)
            link_infos.append(link_info.info())

        # 相关影视/猜你喜欢列表
        related_resources = []
        recommended_resources = []
        for movie_rel_div in movie_soup.find_all('div', class_='movie_rel'):
            ul_tag = movie_rel_div.find('ul', id='related_movies')
            if ul_tag is None:
                continue

            li_tags = ul_tag.find_all('li')
            if li_tags is None or len(li_tags) <= 0:
                continue

            rel_resources = []
            for li in li_tags:
                resource_title = li.text
                resouces_movie_link = li.a['href'] if li.a is not None else ''
                resouces_info = ResourceInfo(title=resource_title, movie_link=resouces_movie_link)
                rel_resources.append(resouces_info.info())

            rel_cat_title = movie_rel_div.find('h2').text
            if rel_cat_title == '相关影视':
                related_resources = rel_resources
            elif rel_cat_title == '猜你喜欢':
                recommended_resources = rel_resources

        # 剧情简介
        story_tag = movie_soup.find('p', id='movie_info')
        story = story_tag.text.strip('\n').strip() if story_tag is not None else ''
        story = '\n'.join([line.strip('\n').strip() for line in story.split('\n')])

        movie_info = MovieInfo(title=title, banner=banner, directors=directors, writers=writers, stars=stars,
                               genres=genres, country=country, release_date=release_date, runtime=runtime,
                               akaname=akaname, star=star, story=story, links=link_infos,
                               related_resources=related_resources, recommended_resources=recommended_resources)

        return success({
            "movie": movie_info.info()
        })

    def __repr__(self):
        return "%s" % self.__class__.__name__
