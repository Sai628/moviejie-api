# coding=utf-8

from __future__ import print_function
import json
import os

from bs4 import BeautifulSoup
import requests
import requests.packages.urllib3

from config import config
from util import const
from util import log


requests.packages.urllib3.disable_warnings()


def get_html(url):
    try:
        response = requests.get(url, verify=False, headers=config.SIMULATE_HEADERS, cookies=config.LOGIN_COOKIES)
        return response.text
    except Exception as e:
        print_error("Error: %s\n get_url_content -- %s" % (e, url))
        return None


def get_html_soup(url):
    html = get_html(url)
    return get_soup(html)


def get_soup(html):
    return BeautifulSoup(html, "lxml")


def send_request(url, json_data):
    try:
        headers = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.post(url=url, json=json_data, headers=headers, verify=False)
        return response.text
    except Exception as e:
        print_error("Error: %s\nsend_post_requestion -- %s" % (e, url))
        return None


def save_content_to_file(file_path, content):
    f = open(file_path, 'a')
    f.write(content)
    f.close()


def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def print_error(text):
    print('\033[0;31;40m%s' % text)


def json_dumps(content):
    return json.dumps(content, ensure_ascii=False)


def success(info=None, max_log_len=2000):
    if info is None:
        info = {}
    info["status"] = const.STATUS_SUCCESS
    response_body = json_dumps(info)
    log.debug("response:%s", response_body[0:max_log_len])
    return json.loads(response_body)


def fail(info=None, max_log_len=2000):
    if info is None:
        info = {}
    info["status"] = const.STATUS_FAIL
    response_body = json_dumps(info)
    log.debug("response:%s", response_body[0:max_log_len])
    return json.loads(response_body)


def get_p_text(tag, class_name):
    return get_tag_child_text(tag, child_tag_name='p', class_name=class_name)


def get_span_text(tag, class_name):
    return get_tag_child_text(tag, child_tag_name='span', class_name=class_name)


def get_tag_child_text(tag, child_tag_name, class_name):
    child_tag = tag.find(child_tag_name, class_=class_name)
    if child_tag is not None:
        text_list = child_tag.text.split('：')[1:]
        return ''.join(text_list).strip()
    return ''
