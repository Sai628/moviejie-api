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
    'Hm_lpvt_85abf7488e97713e5a0e152b2ab2316d': '1532933626',
    'Hm_lvt_85abf7488e97713e5a0e152b2ab2316d': '1532933066',
    'user_nickname': '"2|1:0|10:1532933138|13:user_nickname|8:U2FpNjI4|f19cba12c47546f3f2f937450fac37bfa45da4292c71307ad7c801466eb04494"',
    'user_slug': '"2|1:0|10:1532933138|9:user_slug|8:YzI3Yzc0|82f6d08029b856098f9f26fa6001d199265d7960ff9b770387f778455b60420f"',
    '_xsrf': '2|7dafcf54|c0dfd3d6cded55d1c16c0122d24f91f5|1532933065',
}
