# coding=utf-8

import time

from flask_restful import Resource

from app import cache
from config import config
from model import LinkDetailInfo
from selenium import webdriver
from util.helper import *


class Link(Resource):
    @cache.memoize(timeout=config.CACHE_EXPIRE_TIME)
    def get(self, link_id):
        link_soup = get_html_soup('%s/link/%s' % (config.API_DOMAIN, link_id))

        # 电影页面链接
        movie_title = ''
        movie_link = ''
        movie_back_div = link_soup.find('div', class_='movie_back')
        if movie_back_div is not None:
            movie_back_a_tag = movie_back_div.a
            if movie_back_a_tag is not None:
                movie_title = movie_back_a_tag.text.strip()
                movie_link = movie_back_a_tag['href']

        # 下载资源名称
        link_info_div = link_soup.find('div', class_='link_info')
        p_tags = link_info_div.find_all('p')
        name = p_tags[0].text.split('：')[1].strip()
        size = p_tags[1].text.split('：')[1].strip()

        # 下载链接地址
        link_parsed_html = ''
        for script_tag in link_soup.find_all('script'):
            if '~[]' in script_tag.text:  # 包括 "~[]" 字符的 javascript 代码, 为生成下载链接的代码
                get_link_html = '<span id="link_text_span"></span>' + \
                                '<script type="text/javascript">' + script_tag.text + '</script>'
                temp_file_path = '%s-%.9f.html' % (link_id, time.time())
                save_content_to_file(temp_file_path, get_link_html)
                
                driver = webdriver.PhantomJS()
                driver.get(temp_file_path)
                link_parsed_html = driver.page_source
                driver.close()

                remove_file(temp_file_path)

        link_parsed_soup = get_soup(link_parsed_html)
        link_tag = link_parsed_soup.find('span', id='link_text_span')
        download_link = link_tag.text.strip() if link_tag is not None else ''
        link_detail_info = LinkDetailInfo(movie_title=movie_title, movie_link=movie_link, name=name, size=size,
                                          download_link=download_link)

        return success({
            "link_detail": link_detail_info.info()
        })

    def __repr__(self):
        return "%s" % self.__class__.__name__
