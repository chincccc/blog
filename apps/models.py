from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from flask import current_app

from app import db, login_manager



class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.String(20), primary_key=True)
    user_name = db.Column(db.String(30), unique=True)
    nickname = db.Column(db.String(40), unique=True)
    sex = db.Column(db.String(4))
    age = db.Column(db.Integer)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(50), unique=True)
    birthdate = db.Column(db.Date)
    user_crt_dt = db.Column(db.DateTime)
    attention_cnt = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<{},{},{}>'.format(self.user_name, self.email, self.user_id)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.user_id

    def generate_auth_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'user_id': self.user_id}).decode("utf-8")

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception:
            return None
        return User.query.get(data['user_id'])


class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.Column(db.String(20), primary_key=True)
    article_title = db.Column(db.String(100), nullable=False)
    article_text = db.Column(db.Text)
    article_summary = db.Column(db.String(255))
    article_read_cnt = db.Column(db.Integer, default=0)
    article_sc = db.Column(db.Integer, default=0)
    article_pl = db.Column(db.Integer, default=0)
    article_date = db.Column(db.DateTime)
    article_url = db.Column(db.Text)
    article_type = db.Column(db.String(10))
    article_author = db.Column(db.String(20))
    user_id = db.Column(db.String(20))


class Comment(db.Model):
    __tablename__ = 'comment'
    comment_id = db.Column(db.String(20), primary_key=True)
    comment_text = db.Column(db.Text)
    comment_date = db.Column(db.DateTime)
    comment_name = db.Column(db.String(30))
    comment_support = db.Column(db.Integer, default=0)
    comment_oppose = db.Column(db.Integer, default=0)
    article_id = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.String(20))


class Task(db.Model):
    __tablename__ = "task"
    task_id = db.Column(db.String(20), primary_key=True)
    task_name = db.Column(db.String(50), nullable=False)
    start_dt = db.Column(db.String(16))
    content = db.Column(db.String(200))
    stat = db.Column(db.String(10), default='进行中')
    user_id = db.Column(db.String(20))


class Commparam(db.Model):
    __tablename__ = 'commparam'
    param_name = db.Column(db.String(10), primary_key=True)
    param_value = db.Column(db.Integer, default=1)
    param_text = db.Column(db.String(100))
    param_stat = db.Column(db.String(2), default='0')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
