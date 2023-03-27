from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from puppycompanyblog import db
from puppycompanyblog.models import BlogPost
from puppycompanyblog.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)

# CREATE
@blog_posts.route('/create',methods = ['GET','POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data, text = form.text.data, user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)


# Show BLOG POST
@blog_posts.route('/<int:blog_post_id>') # make sure the id is integer instead of string. So when we query the blogpost from database, the method will not get confused
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id) 
    return render_template('blog_post.html', title=blog_post.title, date =blog_post.date, post=blog_post)

# UPDATE
@blog_posts.route('/<int:blog_post_id>/update', methods=['GET','POST'])
@login_required
def update(blog_post_id):
    # make sure the author is the current user, so only author could update the post
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403) # allow us pass in common error code
    form = BlogPostForm()

    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.text = form.text.data
        
        db.session.commit() # we don't need to add it to database, just commit it is fine
        flash('Blog Post Updated')
        return redirect(url_for('blog_posts.blog_post', blog_post_id=blog_post.id))
    # make sure when the user first view this page, the original blog title and text would be pre-filled in the form
    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text
    return render_template('create_post.html', title='Updating',form=form)

# DELETE
# we don't need a html to delete, we just need a button on the nav bar to allow us click to delete the post
@blog_posts.route('/<int:blog_post_id>/delete', methods=['GET','POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)
    
    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('core.index'))