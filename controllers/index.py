# coding=utf-8

from flask_restful import Resource

from util.helper import *
from config import config
from model import ResourceInfo, IndexInfo


class Index(Resource):
    def get(self):
        index_soup = get_html_soup(config.API_DOMAIN)
        cat_titles = [tag.text for tag in index_soup.find_all('h4')]
        cat_titles = filter(lambda x: "更新" in x, cat_titles)  # 过滤出包含"更新"的类别

        index_infos = []
        tbody_tags = [tag for tag in index_soup.find_all('tbody')[:len(cat_titles)]]
        for index, tbody_tag in enumerate(tbody_tags):
            tr_tags = tbody_tag.find_all('tr')
            resources = []
            for tr in tr_tags:
                # 获取资源(电影/电视剧)的标题
                title = tr.find('span', {'class': 'restitle'}).text.strip()
                title = title.replace('【电影】', '')
                title_a_tag = tr.find('span', {'class': 'restitle'}).a
                if title_a_tag is not None:
                    title_a_text = title_a_tag.text.strip()
                    title = title.replace(title_a_text, '').strip()

                # 获取资源的大小
                size = tr.find('td', {'class': 'size'}).text

                # 获取资源的下载链接页面地址
                link_tag = tr.find('td', {'class': 'link'}).a
                if link_tag is not None:
                    link = link_tag['href']

                # 获取资源的合集页面地址
                movie_link_tag = tr.find('span', {'class': 'restitle'}).a
                if movie_link_tag is not None:
                    movie_link = movie_link_tag['href']

                resource_info = ResourceInfo(title=title, size=size, movie_link=movie_link, link=link)
                resources.append(resource_info.info())

            index_info = IndexInfo(category=cat_titles[index], resources=resources)
            index_infos.append(index_info.info())

        return success({
            "indexInfos": index_infos
        })
