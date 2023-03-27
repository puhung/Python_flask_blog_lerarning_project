from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from puppycompanyblog import db # go to puppycompanyblog/__init__.py to grab db 
from puppycompanyblog.models import User, BlogPost
from puppycompanyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from puppycompanyblog.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)

# register
@users.route('/register', methods=['GET','POST']) # since we are using forms, we need to add methods
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        # the form itself will check 
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

# login
@users.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('core.index')
            
            return redirect(next)
    return render_template('login.html',form=form)

# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index')) # we can't just call index since we are using blueprint

# account (update UserForm)
@users.route('/account', methods=['GET','POST'])
@login_required
def account():

    form = UpdateUserForm()
    if form.validate_on_submit():
        # if user upload the data
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')

        return redirect(url_for('users.account'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static',filename='profile_pics/'+current_user.profile_image) 
    return render_template('account.html', profile_image = profile_image, form=form)

# user's list of Blog posts
@users.route('/<username>') #username will change
def user_posts(username):
    page = request.args.get('page',1,type=int) # cycle thorugh user posts using pages
    user = User.query.filter_by(username=username).first_or_404() # grab the user if user exist or return 404 error

    # the foreign key relationship in models.py is called author
    # query all the blog posts where the author is equal to the user, then order the blog post by descending order
    # filter_by and order_by is function from SQLAlchemy 
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page = 5) 
    return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)


