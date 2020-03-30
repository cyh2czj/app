import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

DATABASE_QUERY_TIMEOUT = 0.00001
SQLALCHEMY_RECORD_QUERIES = True

class Config():
    SECRET_KEY = 'canyouguess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Cyh920610.@127.0.0.1/WEB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN = 'hao512991349@qq.com'
    FLASKY_POSTS_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 20
    FLASK_POSTS_PER_PAGE = 20
    FLASK_FOLLOWERS_PER_PACE = 20

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
