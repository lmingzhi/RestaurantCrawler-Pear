# coding=utf-8

import logging

from flask import Flask
from pear.utils.config import IS_DEBUG

app = Flask(__name__)
logging.basicConfig(format='%(levelname)s %(asctime)s %(filename)s %(lineno)d %(message)s', level=logging.INFO)


@app.route("/check_health", methods=["GET"])
def check_health():
    return 'OK'


def install_modules(app):
    from pear.web.handlers.crawler import crawlers_router
    from pear.web.handlers.data_analyse import data_router
    from pear.web.handlers.user import user_router
    app.register_blueprint(crawlers_router)
    app.register_blueprint(data_router)
    app.register_blueprint(user_router)


def init_app():
    install_modules(app)
    app.secret_key = "pear_web_secret_key"
    return app


def main():
    init_app()
    app.run(debug=IS_DEBUG)
