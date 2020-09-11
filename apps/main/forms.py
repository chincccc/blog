from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, TextField, DateField, FloatField, SubmitField,IntegerField,RadioField
from wtforms.validators import DataRequired, Length, email,NumberRange

class LoginForm(FlaskForm):
    username = StringField(
        label='用户昵称',
        validators=[
            DataRequired("昵称必填"),
            Length(min=4, max=20, message="用户名必须介于4-20个字符")
        ],
        render_kw={"placeholder": "用户名必须介于4-20个字符"})
    password = PasswordField(
        label="用户密码",
        validators=[DataRequired("密码必填！")],
        render_kw={
            "placeholder": '密码必须大于6个字符',
        })
    submit = SubmitField(label='登录')


class RegisterForm(FlaskForm):
    username = StringField(
        label='登录用户名',
        validators=[
            DataRequired("用户名必填"),
            Length(min=4, max=20, message="4-20个字符")
        ],
        render_kw={"placeholder": "用户名必须介于4-20个字符"})
    nickname = StringField(
        label='昵称',
        validators=[
            DataRequired("昵称必填"),
            Length(min=1, max=20, message="昵称必须介于1-20个字符")
        ],
        render_kw={"placeholder": "1-20个字符"})
    sex = RadioField('性别', choices=[('男','男'),('女','女')],validators=[DataRequired("性别必填！")])
    password = PasswordField(
        label="用户密码",
        validators=[DataRequired("密码必填！")],
        render_kw={
            "placeholder": '密码必须大于6个字符',
        })
    password2 = PasswordField(
        label="用户密码",
        validators=[DataRequired("密码必填！")],
        render_kw={
            "placeholder": '再次输入',
        })
    email = StringField(
        '邮箱',
        validators=[email(message="邮箱格式不正确！")],
        render_kw={"placeholder": "xxxx@xxxx.com"})
    birthdate = DateField(
        label='生日',
        validators=[DataRequired('日期格式不正确')],
        render_kw={"placeholder": "日期如：2020-06-06"})
    age = IntegerField(
        label='年龄',
        validators=[NumberRange(min=0, max=150, message="年龄需要在0-150岁內")],
        render_kw={"placeholder": "年龄:0-150岁"})
    submit = SubmitField(label='注册')

class PassForm(FlaskForm):
    passold = PasswordField(
        label="原先密码",
        validators=[DataRequired("密码必填")],
        render_kw={
            "placeholder": '密码必须大于6个字符',
        })
    password = PasswordField(
        label="新密码",
        validators=[DataRequired("密码必填")],
        render_kw={
            "placeholder": '密码必须大于6个字符',
        })
    password2 = PasswordField(
        label="再输入一次新密码",
        validators=[DataRequired("密码必填！")],
        render_kw={
            "placeholder": '再次输入',
        })
    submit = SubmitField(label='修改')


class MyselfForm(FlaskForm):
    username = StringField(
        label='登录用户名',
        validators=[
            DataRequired("用户名必填"),
            Length(min=4, max=20, message="4-20个字符")
        ],
        render_kw={"placeholder": "用户名必须介于4-20个字符"})
    nickname = StringField(
        label='昵称',
        validators=[
            DataRequired("昵称必填"),
            Length(min=1, max=20, message="昵称必须介于1-20个字符")
        ],
        render_kw={"placeholder": "1-20个字符"})
    sex = RadioField('性别', choices=[('男', '男'), ('女', '女')], validators=[DataRequired("性别必填！")])
    email = StringField(
        '邮箱',
        validators=[email(message="邮箱格式不正确！")],
        render_kw={"placeholder": "xxxx@xxxx.com"})
    birthdate = DateField(
        label=' 生日',
        validators=[DataRequired('日期格式不正确')],
        render_kw={"placeholder": "日期如：2020-06-06"})
    age = IntegerField(
        label='年龄',
        validators=[NumberRange(min=0, max=150, message="年龄需要在0-150岁內")],
        render_kw={"placeholder": "年龄:0-150岁"})
    submit = SubmitField(label='修改')
