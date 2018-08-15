from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp


class PostForm(FlaskForm):
    name = TextAreaField("Name", validators=[DataRequired()])
    desc = TextAreaField("content", validators=[DataRequired()], render_kw={"id": "t2", "rows": "10"})
    body = TextAreaField("content", validators=[DataRequired()], render_kw={"id":"t1","rows":"10"})
    cate = SelectField('cate', validators=[DataRequired()], choices=[('1', 'flsk'), ('2', '杂谈'), ('3', 'scasca'), ('4', '好爱吃亏了几百次'), ('5', 'dw21d'), ('6', '妻儿传奇而完成全部ＩＣ了吧'), ('7', 'eqcqwechcbqwd'), ('8', '擦去完成前完成即可能领取'), ('9', 'wcqwcqwkjc'), ('10', '出去玩出去玩吧'), ('1', 'flsk'), ('2', '杂谈' 'dw21d'), ('6', '妻儿传奇而完成全部ＩＣ了吧'), ('7', 'eqcqwechcbqwd'), ('8', '擦去完成前完成即可能领取'), ('9', 'wcqwcqwkjc'), ('10', '出去玩出去玩吧')])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    name = StringField(
        label="账号",
        validators=[
            DataRequired("账号不能为空！")
        ],
        description="账号",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入账号！",
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空！")
        ],
        description="密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block",
        }
    )


class CommentForm(FlaskForm):
    body = TextAreaField("添加评论", validators=[DataRequired()])
    submit = SubmitField('Submit')


class CateForm(FlaskForm):
    body = TextAreaField("Category", validators=[DataRequired()])
    submit = SubmitField('Submit')