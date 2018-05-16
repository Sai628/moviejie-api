# coding=utf-8

import sys

from flask import Flask
from flask_cache import Cache
import flask_restful as restful


# 解决输出中文报错 UnicodeEncodeError 的问题
reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)
api = restful.Api(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


import controllers
api.add_resource(controllers.Index, '/')
api.add_resource(controllers.Movie, '/movie/<string:movie_id>/')
api.add_resource(controllers.Link, '/link/<string:link_id>/')
api.add_resource(controllers.OST, '/ost/<string:ost_id>/')
api.add_resource(controllers.NewMovie, '/new/movie/<string:page>/')
api.add_resource(controllers.NewTv, '/new/tv/<string:page>/')
api.add_resource(controllers.NewOST, '/new/ost/<string:page>/')
api.add_resource(controllers.Search, '/search/<string:keyword>/<string:page>/')
