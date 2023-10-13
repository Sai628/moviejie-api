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
    'hide_slogan': '1694158765809',
    'user_nickname': '2|1:0|10:1697175695|13:user_nickname|8:U2FpNjI4|02fc53efd2edfa37010976d37a683b0bd260fe4349fe4bb327e7917640dec725',
    'user_slug': '2|1:0|10:1694158707|9:user_slug|8:YzI3Yzc0|f0d65da50e8ca7ef633675481d3ba19adddadb6df87527c9bcad670ba3f1920e',
    'user_nickname': '2|1:0|10:1694158707|13:user_nickname|8:U2FpNjI4|e5506a1831abd808ff6e5b2c0ff632abf60e8777f009a3b556e1464a047ae201',
    'user_slug': '2|1:0|10:1697175695|9:user_slug|8:YzI3Yzc0|d26ca075cf37aa002bec3c98dde16b178c206dcb683a53a6894f3a926fbdb4b9',
    '_xsrf': '2|5b24ffcb|c30658fc959a97fa2ce2a295e2030584|1694158698',
    '_xsrf': '2|ec8cf54d|da3f8ae06d188998039700391e753a49|1697175621',
}
