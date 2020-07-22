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