from datetime import datetime
from . import db
from flask import url_for

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    desc = db.Column(db.Text)
    body = db.Column(db.Text)
    time_add = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    cate_id = db.Column(db.Integer, db.ForeignKey('category.id'))


    def to_json(self):
        json_post = {
            'url': url_for('api.get_posts', id=self.id),
            'body': self.body,
            'name': self.name,
            'desc': self.desc,
            'time_add': self.time_add,
        }
        return json_post

    @staticmethod
    def from_json(json_post):
        body = json_post.get('body')
        if body is None or body == '':
            return ('post does not have a body')
        return Post(body=body)



class Category(db.Model):
    __tablename__='category'
    id = db.Column(db.Integer, primary_key=True)
    cate = db.Column(db.Text)


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


class Comment(db.Model):
    __tablename__='comment'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    time_add = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    post_doc_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def to_json(self):
        json_post = {
            'url': url_for('api.get_post_comments', id=self.id),
            'body': self.body,
            'time_add': self.time_add,
        }
        return json_post
