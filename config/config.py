# coding=utf-8

# 缓存到期时间(单位:秒)
CACHE_EXPIRE_TIME = 1800

# API地址
API_DOMAIN = 'https://moviejie.net'
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
    '_ga': 'GA1.2.14896441.1509380435',
    '_xsrf': '2|d68f7930|5509740495ec4f2d0885c6b0220e06d7|1516465214',
    'Hm_lvt_85abf7488e97713e5a0e152b2ab2316d': '1516465217',
    'user_slug': '"2|1:0|10:1516465397|9:user_slug|8:YzI3Yzc0|60f6dde59909a5c7efd954d09fbc2623aa9ca6e303409ccebee0c49cfec25bf1"',
    'user_nickname': '"2|1:0|10:1516465397|13:user_nickname|8:U2FpNjI4|6a67a839ea7fb9b1cc94102f62cf00624f99fd5b25b523be9f9b42d5cd80a1f4"',
    'Hm_lpvt_85abf7488e97713e5a0e152b2ab2316d': '1516465398',
}
