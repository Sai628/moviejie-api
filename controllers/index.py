# coding=utf-8

from flask_restful import Resource

from app import cache
from util.helper import *
from config import config
from model import ResourceInfo, NewInfo, HotInfo


class Index(Resource):
    @cache.memoize(timeout=config.CACHE_EXPIRE_TIME)
    def get(self):
        index_soup = get_html_soup(config.API_INDEX)

        # 解析更新资源
        new_info_div = index_soup.find('div', class_='link_list')
        new_cat_titles = [tag.text for tag in new_info_div.find_all('h4')]

        new_infos = []
        tbody_tags = [tag for tag in new_info_div.find_all('tbody')[:len(new_cat_titles)]]
        for index, tbody_tag in enumerate(tbody_tags):
            resources = []
            for tr in tbody_tag.find_all('tr'):
                # 获取资源(电影/电视剧)的标题
                title = tr.find('span', class_='restitle').text.strip()
                title = title.replace('【电影】', '').strip()
                title_a_tag = tr.find('span', class_='restitle').a
                if title_a_tag is not None:
                    title_a_text = title_a_tag.text.strip()
                    title = title.replace(title_a_text, '').strip()

                # 获取资源的大小
                size = tr.find('td', class_='size').text

                # 获取资源的下载链接页面地址
                link_tag = tr.find('td', class_='link').a
                if link_tag is not None:
                    link = link_tag['href']

                # 获取资源的合集页面地址
                movie_link_tag = tr.find('span', class_='restitle').a
                movie_link = movie_link_tag['href'] if movie_link_tag is not None else ''

                resource_info = ResourceInfo(title=title, movie_link=movie_link, link=link, size=size)
                resources.append(resource_info.info())

            new_info = NewInfo(category=new_cat_titles[index], resources=resources)
            new_infos.append(new_info.info())

        # 解析热门/最新资源
        hot_info_divs = index_soup.find_all('div', class_='movie_list')
        hot_infos = []
        for div in hot_info_divs:
            resources = []
            for li in div.find_all('li'):
                title_a_tag = li.find('div', class_='infos').a
                title = title_a_tag.text.strip()  # 获取资源标题
                movie_link = title_a_tag['href']  # 获取资源链接

                # 获取资源评分
                rating_tag = li.find('span', class_='star')
                rating = rating_tag.text if rating_tag is not None else ""

                resource_info = ResourceInfo(title=title, movie_link=movie_link, rating=rating)
                resources.append(resource_info.info())

            hot_cat_title = div.find('h4').text
            hot_info = HotInfo(category=hot_cat_title, resources=resources)
            hot_infos.append(hot_info.info())

        return success({
            "news": new_infos,
            "hots": hot_infos
        })

    def __repr__(self):
        return "%s" % self.__class__.__name__
