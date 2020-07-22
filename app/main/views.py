from flask import render_template, request, redirect, url_for,abort
from . import main
from .forms import PostPitch, CategoryForm. CommentForm
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


    

# @main.route('/user/<uname>')
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()

#     if user is None:
#         abort(404)

#     return render_template("profile/profile.html", user = user)