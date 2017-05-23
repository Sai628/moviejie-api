# coding=utf-8

from flask_restful import Resource as RESTfulResource

from util.helper import *
from config import config
from model.resource import Resource


class Index(RESTfulResource):
    def get(self):
        index_soup = get_html_soup(config.API_DOMAIN)
        cat_titles = [tag.text for tag in index_soup.find_all('h4')]
        cat_titles = filter(lambda x: "更新" in x, cat_titles)

        result = []
        tbody_tags = [tag for tag in index_soup.find_all('tbody')[:len(cat_titles)]]
        for index, tbody_tag in enumerate(tbody_tags):
            tr_tags = tbody_tag.find_all('tr')
            resources = []
            for tr in tr_tags:
                title = tr.find('span', {'class': 'restitle'}).text.strip()
                title = title.replace('【电影】', '')
                title_a_tag = tr.find('span', {'class': 'restitle'}).a
                if title_a_tag is not None:
                    title_a_text = title_a_tag.text.strip()
                    title = title.replace(title_a_text, '').strip()

                size = tr.find('td', {'class': 'size'}).text

                link_tag = tr.find('td', {'class': 'link'}).a
                if link_tag is not None:
                    link = link_tag['href']
                movie_link_tag = tr.find('span', {'class': 'restitle'}).a
                if movie_link_tag is not None:
                    movie_link = movie_link_tag['href']

                res = Resource(title=title, size=size, movie_link=movie_link, link=link)
                resources.append(res.info())

            item = {'update_date': cat_titles[index], "resources": resources}
            result.append(item)

        return success({
            "result": result
        })
