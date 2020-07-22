from flask import render_template, request, redirect, url_for,abort
from flask_login import login_required, current_user
from . import main
from .forms import PostPitch, CategoryForm, CommentForm
from  ..import db

from ..models import Pitch,User,Comments,Category

#Views 
@main.route('/')

def index():
    '''
    View functions that displays the home page
    '''
    title = 'Welcome to largest repositories of pitches'
    categories =Category.get_categories()
    pitches = Pitch.query.order_by('id').all()
    print(pitches)

    return render_template('index.html', pitches=pitches, categories = categories)


#Route for new Pitch

@main.route('/post/new-pitch/<int:id>',methods = ['GET','POST'])
@login_required
def pitch_page(id):

    form = PostPitch()
    category = Category.query.filter_by(id=id).first()
    '''
    Function to render page that displays individual page for the pitch
    '''
    title = 'Welcome to largest business networking site'
    
    if category is None:
        abort(404)
    if form.validate_on_submit():
        
        pitch =form.pitch.data
        new_pitch = Pitch(pitch=pitch,category_id=category.id,user_id = user.id)
        print(new_pitch)
        new_pitch.save_pitches()
        return redirect(url_for('.category',id= category_id.id ))
    return render_template('pitch.html',category = category,pitch_form=form)

#Route to categories Pitchlist
@main.route('/categories/<int:id>')
def category(id):
    category = PitchCategory.query.get(id)
    if category is None:
        abort(404)

    pitches=Pitch.get_pitches(id)
    return render_template('category.html', pitches=pitches, category=category)

#Route to create a new category
@main.route('/create/category', methods=['GET','POST'])
@login_required
def new_category():
    """
    View new group route function that returns a page with a form to create a category
    """
    
    form = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        new_category = Category(name = name)
        new_category.save_category()

        return redirect(url_for('.index'))

    title = 'New category'
    return render_template('new_category.html', category_form = form, title = title)

#Route to view single pitch plus its comments
@main.route('/view-pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):
    """
    Function the returns a single pitch with comment section
    """
    category = Category.get_categories()
    pitches = Pitch.query.get(id)
    

    if pitches is None:
        abort(404)
    
    comment = Comments.get_comments(id)
    
    return render_template('view-pitch.html', pitches = pitches, comment = comment, category_id = id, categories=category)


#Rout to add a new comment
@main.route('/new-comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    """ 
    Function to post new comments on our pitches
    """
    
    form = CommentForm()
    title = 'post comment'
    pitches = Pitch.query.filter_by(id=id).first()

    if pitches is None:
        abort(404)

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comments(comment = comment, user_id = current_user.id, pitches_id = pitches.id)
        new_comment.save_comments()
        return redirect(url_for('.view_pitch', id = pitches.id))

    return render_template('new-comment.html', comment_form = form, title = title)