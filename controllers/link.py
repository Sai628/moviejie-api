# coding=utf-8

import os
import time

from flask_restful import Resource

from app import cache
from util.helper import *
from config import config
from selenium import webdriver


class Link(Resource):
    @cache.memoize(timeout=config.CACHE_EXPIRE_TIME)
    def get(self, link_id):
        link_soup = get_html_soup(config.API_DOMAIN + '/link/' + link_id)
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
        link = link_tag.text.strip() if link_tag is not None else ''

        return success({
            "link": link
        })

    def __repr__(self):
        return "%s" % self.__class__.__name__
