# coding=utf-8

from __future__ import print_function
import json

from bs4 import BeautifulSoup
import requests

from util import const
from util import log


def get_html(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        my_print_error("Error: %s\nget_url_content -- %s" % (e, url))
        return None


def get_html_soup(url):
    html = get_html(url)
    return BeautifulSoup(html, "lxml")


def send_request(url, json_data):
    try:
        headers = {"Content-Type": "application/json; charset=utf-8"}
        response = requests.post(url=url, json=json_data, headers=headers)
        return response.text
    except Exception as e:
        my_print_error("Error: %s\nsend_post_requestion -- %s" % (e, url))
        return None


def my_print(text, debug=True):
    if debug:
        print(text)


def my_print_error(text):
    print('\033[0;31;40m%s' % text)


def json_dumps(content):
    return json.dumps(content, ensure_ascii=False)


def success(info=None, max_log_len=2000):
    if info is None:
        info = {}
    info["status"] = const.STATUS_SUCCESS
    response_body = json_dumps(info)
    log.debug("response:%s", response_body[0:max_log_len])
    return info


def fail(info=None, max_log_len=2000):
    if info is None:
        info = {}
    info["status"] = const.STATUS_FAIL
    response_body = json_dumps(info)
    log.debug("response:%s", response_body[0:max_log_len])
    return info
