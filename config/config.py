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
    'Hm_lpvt_85abf7488e97713e5a0e152b2ab2316d': '1548736642',
    'Hm_lvt_85abf7488e97713e5a0e152b2ab2316d': '1548251672,1548562921',
    'user_nickname': '"2|1:0|10:1548736641|13:user_nickname|8:U2FpNjI4|cc259a2f729b7016d6f81d086f1f1618514a0f3563128b2ad37133e815aad204"',
    'user_slug': '"2|1:0|10:1548736641|9:user_slug|8:YzI3Yzc0|e833bd327a536f6e3efcd63f4eac2960cdc583992851aa64a0ee79649a543af1"',
    '_xsrf': '2|1d48a1fb|db61923fe06765f0dc1dd9b41a9549c0|1548562918',
}
