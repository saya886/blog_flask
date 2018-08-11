from functools import wraps

from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response, session
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
from . import main
from .. import db
from .forms import PostForm, LoginForm
from ..models import Post, User
from werkzeug.security import generate_password_hash, check_password_hash


def user_login_req(f):
    """
    登录装饰器
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for(".login"))
        return f(*args, **kwargs)

    return decorated_function


@main.route('/', methods=['GET','POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    posts = Post.query.all()
    return render_template('index.html',form=form,posts=posts)


@main.route("/login/", methods=["GET", "POST"])
def login():
    """
    登录
    """
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data["name"]).first()
        if user:
            if not user.check_pwd(data["pwd"]):
                flash("密码错误！", "err")
                return redirect(url_for(".login"))
        else:
            flash("账户不存在！", "err")
            return redirect(url_for(".login"))
        session["user"] = user.name
        session["user_id"] = user.id
        return redirect(url_for(".index"))
    return render_template("login.html", form=form)


@main.route("/logout/")
def logout():
    """
    退出登录
    """
    # 重定向到home模块下的登录。
    session.pop("user", None)
    session.pop("user_id", None)
    return redirect(url_for('.login'))

@main.route("/add/", methods=['GET','POST'])
@user_login_req
def add():
    """
    添加文章
    """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template('add.html',form=form)
