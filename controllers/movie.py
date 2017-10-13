# coding=utf-8

from flask_restful import Resource

from util.helper import *
from config import config
from model import MovieInfo, LinkInfo, ResourceInfo


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
        runtime = get_info_text(infos_div, 'runtime')
        akaname = get_info_text(infos_div, 'akaname')
        star = get_info_text(infos_div, 'star')

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

        movie_info = MovieInfo(title=title, banner=banner, directors=directors, writers=writers, stars=stars,
                               genres=genres, country=country, release_date=release_date, runtime=runtime,
                               akaname=akaname, star=star, story=story, links=link_infos,
                               related_resources=related_resources, recommended_resources=recommended_resources)

        return success({
            "movie": movie_info.info()
        })


def get_info_text(tag, class_name):
    p_tag = tag.find('p', class_=class_name)
    return p_tag.text.split('：')[1].strip() if p_tag is not None else ''
