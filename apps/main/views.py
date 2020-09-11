import re
import time
import markdown
from datetime import datetime, timedelta
from flask import g
from flask import(redirect, render_template,request, url_for, flash)
from flask_login import login_required, current_user, login_user, logout_user

from . import main
from ..models import User, Article, Comment, Task, db
from .forms import LoginForm, RegisterForm,MyselfForm,PassForm
from ..tools import generate_id

@main.before_request
def before_request():
    g.user = current_user

@main.route('/')
def index():
    articles = Article().query.all()
    return render_template('index.html', articles=articles, flag=0)


@main.route('/login_in/', methods=['POST', 'GET'])
def login_in():
    loginForm = LoginForm()
    error=None
    if loginForm.validate_on_submit():
        username = loginForm.username.data
        password = loginForm.password.data
        user = User.query.filter_by(user_name=username).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            g.user=None
    if loginForm.validate_on_submit():
        username = loginForm.username.data
        password = loginForm.password.data
        user = User.query.filter_by(user_name=username).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            g.user=user
            g.first = g.user.user_id
            return redirect(url_for('main.index'))
        else:
            error="帐号或密码错误"

    return render_template('login.html', form=loginForm, action='/login_in/',error=error)



@main.route('/login_up/', methods=['GET', 'POST'])
def login_up():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        username = registerForm.username.data
        email = registerForm.email.data
        ubyname = User.query.filter_by(user_name=username).first()
        ubyemail = User.query.filter_by(email=email).first()
        passwd1 = registerForm.password.data
        passwd2 = registerForm.password2.data
        birthdate=registerForm.birthdate.data
        dt = str(time.strftime('%Y-%m-%d %H:%M', time.localtime()))
        age=registerForm.age.data
        sex=registerForm.sex.data
        user = User(user_name=username, email=email, password=passwd1,age=age,birthdate=birthdate,user_crt_dt=dt,sex=sex)
        user.user_id = generate_id('user')
        if ubyname or ubyemail:
            print('用户名或邮箱已存在')
        elif passwd1 != passwd2:
            print('两次密码不一致，请从新输入！')
        else:
            db.session.add(user)
            db.session.commit()
            print('注册成功')
            return redirect(url_for('main.login_in'))
    return render_template('login_up.html', form=registerForm)

@main.route('/user_self/', methods=['GET', 'POST'])
@login_required
def user_self():
    user = User().query.filter_by(user_id=g.user.user_id).all()
    return render_template(
        'user.html', users=user,flag=0)


@main.route('/user_more/<user_id>/', methods=['GET', 'POST'])
def user_more(user_id):
    flag=1
    user = User().query.filter_by(user_id=user_id).all()
    return render_template(
        'user.html', users=user,flag=flag)

@main.route('/user_change/', methods=['GET', 'POST'])
@login_required
def user_change():
    user_id=g.user.user_id
    user = User().query.filter_by(user_id=user_id).first()
    myselfForm = MyselfForm(username=user.user_name,nickname=user.nickname,email=user.email,birthdate=user.birthdate,age=user.age,sex=user.sex)
    if myselfForm.validate_on_submit():
        result=User.query.filter_by(user_id=user_id).first()
        username = myselfForm.username.data
        nickname=myselfForm.nickname.data
        email = myselfForm.email.data
        birthdate = myselfForm.birthdate.data
        sex=myselfForm.sex.data
        age = myselfForm.age.data
        flag=0
        if username != user.user_name:
            ubyname = User.query.filter_by(user_name=username).first()
            print(ubyname)
            if ubyname:
                print("用户名已存在")
                flag=1
        if email != user.email:
            ubyemail = User.query.filter_by(email=email).first()
            if ubyemail:
                print("邮箱已存在")
                flag=1
        if flag==1:
            print('用户名或邮箱已存在，请从新输入！')
        else:
            result.user_name = username
            result.email = email
            result.age = age
            result.sex=sex
            result.birthdate=birthdate
            result.nickname=nickname
            db.session.commit()
            print('修改成功')
            user = User().query.filter_by(user_id=user_id).all()
            return render_template(
                'user.html', users=user)
    return render_template('user_change.html', form=myselfForm)

@main.route('/pass_change/', methods=['GET', 'POST'])
@login_required
def pass_change():
    user_id=g.user.user_id
    user = User().query.filter_by(user_id=user_id).first()
    passForm = PassForm()
    if passForm.validate_on_submit():
        result=User.query.filter_by(user_id=user_id).first()
        oldpass = passForm.passold.data
        passwd1 = passForm.password.data
        passwd2 = passForm.password2.data
        if user is not None and user.verify_password(oldpass):
            if passwd1 != passwd2:
                print('两次密码不一致，请从新输入！')
            else:
                result.password = passwd1
                db.session.commit()
                print('修改成功')
                user = User().query.filter_by(user_id=user_id).all()
                return render_template(
                    'user.html', users=user)
    return render_template('pass_change.html', form=passForm)

@main.route('/login_out')
@login_required
def login_out():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@main.route('/get_article/<article_id>/')
def get_article(article_id):
    article = Article().query.filter_by(article_id=article_id).first()
    article.article_read_cnt = article.article_read_cnt + 1
    db.session.add(article)
    db.session.commit()
    articles = Article().query.limit(8)
    comments = Comment().query.filter_by(article_id=article_id).all()
    return render_template(
        'article.html', article=article, articles=articles, comments=comments)



@main.route('/tasks/')
@login_required
def tasks():
    tasks = Task().query.filter_by(user_id=current_user.user_id).all()
    articles = Article().query.all()
    return render_template('manage_task.html', tasks=tasks,articles=articles, flag=3)


@main.route('/add_task/', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        task_content = request.form.get('task_content')
        task_content = markdown.markdown(task_content, ['extra', 'codehilite'])
        task_id = generate_id('task')
        user_id = current_user.user_id
        start_dt = datetime.now().date()
        task = Task(
            task_id=task_id,
            task_name=task_name,
            start_dt=str(start_dt),
            content=task_content,
            user_id=user_id,
            stat='进行中')
        db.session.add(task)
        db.session.commit()
        print('添加完成')
        tasks = Task().query.filter_by(user_id=user_id).all()
        return render_template('manage_task.html', tasks=tasks)
    else:
        return render_template('add_task.html')


@main.route('/del_task/<task_id>/')
@login_required
def del_task(task_id):
    task = Task().query.filter_by(task_id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    print('删除成功')
    tasks = Task().query.all()
    return render_template('manage_task.html', tasks=tasks, flag=3)

@main.route('/over_task/<task_id>/')
def over_task(task_id):
    task = Task().query.filter_by(task_id=task_id).first()
    task.stat='已完成'
    db.session.add(task)
    db.session.commit()
    tasks = Task().query.all()
    return render_template('manage_task.html', tasks=tasks, flag=3)


@main.route('/wrarticle/', methods=['GET', 'POST'])
@login_required
def wrarticle():
    if request.method == 'POST':
        article_title = request.form.get('article_title')
        artitle_type = request.form.get('f_type')
        article_text = request.form.get('article_content')
        article_url = request.form.get('article_url')
        article_text = markdown.markdown(article_text, ['extra', 'codehilite'])
        article_id = generate_id('article')
        article_date = time.strftime('%Y-%m-%d %H:%M:%S')
        article_type = '科技区' if artitle_type == '1' else '生活区'
        content = re.compile('.*?>(.*?)<').findall(article_text)
        article_summary = ''
        for x in content:
            if x:
                article_summary = article_summary + x
                if len(article_summary) > 250:
                    break

        article_summary = "".join(article_summary.split())
        article = Article(
            article_id=article_id,
            article_title=article_title,
            article_type=article_type,
            article_text=article_text,
            article_summary=article_summary[:180],
            article_url=article_url,
            article_date=article_date,
            user_id=current_user.user_id,
            article_author=current_user.user_name)
        db.session.add(article)
        db.session.commit()
        print('添加成功')
        articles = Article().query.limit(8)
        return render_template(
            'article.html', article=article, articles=articles)
    else:
        return render_template('wrarticle.html')


@main.route('/wrcomment/<article_id>', methods=["POST"])
@login_required
def wrcomment(article_id):
    commentary = request.form.get("commentary")
    commentary = markdown.markdown(commentary, ['extra', 'codehilite'])
    comment_id = generate_id('comment')
    comment_date = time.strftime('%Y-%m-%d %H:%M:%S')
    comment = Comment(
        comment_id=comment_id,
        comment_text=commentary,
        comment_date=comment_date,
        comment_name=g.user.nickname,
        user_id=g.user.user_id,
        article_id=article_id)
    db.session.add(comment)
    db.session.commit()

    article = Article().query.filter_by(article_id=article_id).first()
    article.article_pl = article.article_pl + 1
    db.session.add(article)
    db.session.commit()

    return redirect(url_for("main.get_article", article_id=article_id))

@main.route('/add_article_sc/<article_id>')
def add_article_sc(article_id):
    article = Article().query.filter_by(article_id=article_id).first()
    article.article_sc = article.article_sc + 1
    db.session.add(article)
    db.session.commit()
    articles = Article().query.all()
    return render_template('index.html', articles=articles, flag=0)


@main.route('/comment_oppose/<comment_id>')
def comment_oppose(comment_id):
    comment = Comment().query.filter_by(comment_id=comment_id).first()
    comment.comment_oppose += 1
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/comment_support/<comment_id>')
def comment_support(comment_id):
    comment = Comment().query.filter_by(comment_id=comment_id).first()
    comment.comment_support += 1
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for("main.get_article", article_id=comment.article_id))


@main.route('/del_article/<article_id>/')
@login_required
def del_article(article_id):
    article = Article().query.filter_by(article_id=article_id).first()
    db.session.delete(article)
    comments = Comment().query.filter_by(article_id=article_id).delete(
        synchronize_session=False)
    #db.session.delete(comments)
    db.session.commit()
    print('删除文章成功!!!!')
    return redirect(url_for('main.manage_article'))


@main.route('/manage_article/')
@login_required
def manage_article():
    articles = Article().query.filter_by(user_id=current_user.user_id).all()
    return render_template('manage_article.html', articles=articles)


@main.route('/technology/')
def get_technology():
    articles = Article().query.filter_by(article_type='科技区').all()
    return render_template('index.html', articles=articles, flag=1)


@main.route('/technology2/')
def get_technology2():
    articles = Article().query.filter_by(article_type='生活区').all()
    return render_template('index.html', articles=articles, flag=2)

