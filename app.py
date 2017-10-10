# coding=utf-8

import sys
import traceback

from flask import Flask
import flask_restful as restful


# 解决输出中文报错 UnicodeEncodeError 的问题
reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)
api = restful.Api(app)


def main():
    import controllers
    api.add_resource(controllers.Index, '/')
    api.add_resource(controllers.Movie, '/movie/<string:movie_id>/')
    api.add_resource(controllers.Link, '/link/<string:link_id>/')

    app.run(host='0.0.0.0', port=80, debug=True)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Shutdown app. exiting...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)
