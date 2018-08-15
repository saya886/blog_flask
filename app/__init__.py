from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
import flask_whooshalchemyplus
from flask_whooshalchemyplus import index_all
from jieba.analyse.analyzer import ChineseAnalyzer


app = Flask(__name__)
# 用于连接数据的数据库。
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:rango.lzp@127.0.0.1:3306/blog?charset=utf8"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:tp158917@127.0.0.1:3306/movie"
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SECRET_KEY'] = 'rango.lzp'
app.debug = True
db = SQLAlchemy(app)


bootstrap = Bootstrap(app)

# 不要在生成db之前导入注册蓝图。
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .api import api as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api/v1')

