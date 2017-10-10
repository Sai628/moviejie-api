# coding=utf-8

from flask_restful import Resource

from util.helper import *
from config import config


class Link(Resource):
    def get(self, link_id):
        link_soup = get_html_soup(config.API_DOMAIN + '/link/' + link_id, run_javascript=True)
        link_tag = link_soup.find('span', id='link_text_span')
        link = link_tag.text.strip() if link_tag is not None else ''

        return success({
            "link": link
        })
