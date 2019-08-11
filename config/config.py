# coding=utf-8

# 缓存到期时间(单位:秒)
CACHE_EXPIRE_TIME = 1800

# API地址
API_DOMAIN = 'http://moviejie.xyz'
API_INDEX = API_DOMAIN  # 首页地址
API_NEW_MOVIE = API_DOMAIN + "/new/movie"  # 最新电影地址
API_NEW_TV = API_DOMAIN + "/new/tv"  # 最新电视剧地址
API_NEW_OST = API_DOMAIN + "/new/ost"  # 原声大碟地址
API_NEW_ARTICLE = API_DOMAIN + "/new/article"  # 影评地址
API_SEARCH = API_DOMAIN + "/search"  # 搜索地址

# 模拟的Headers
SIMULATE_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

# 模拟已登录用户对应的Cookies
LOGIN_COOKIES = {
    'Hm_lvt_85abf7488e97713e5a0e152b2ab2316d': '1554270698',
    'user_nickname': '"2|1:0|10:1565254859|13:user_nickname|8:U2FpNjI4|5dada89845c0bf66ec67d06460bc981d4ba94db6a6d3e7a655968e9505c8fc83"',
    'user_slug': '"2|1:0|10:1565254859|9:user_slug|8:YzI3Yzc0|728464ad8897b87d0f1bd749a2a964605574747d6203978b233f483502f59723"',
    '_xsrf': '2|7fb418cd|c2bdacef396cf02f40f5354bea1e59d9|1564287607',
}
