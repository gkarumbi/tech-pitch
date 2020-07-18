from flask import render_template, request, redirect, url_for,abort
from . import main
from .forms import PostPitch

from ..request import create_pitch
from ..models import Pitch,User

#Views 
@main.route('/')

def index():
    '''
    View functions that displays the home page
    '''
    title = 'Welcome to largest business networking site'
    pitch_in_views = create_pitch()

    return render_template('index.html', title = title,pitch_in_html = pitch_in_views)

@main.route('/post/<pitch_url>',methods = ['GET','POST'])

def pitch_page(pitch_url):

    form = PostPitch()

    '''
    Function to render page that displays individual page for the pitch
    '''
    title = 'Welcome to largest business networking site'
    pitch = create_pitch()
    print(pitch)
    if form.validate_on_submit():
        
        #category =form.category.data
        pitch = form.pitch.data
        new_pitch = Pitch(pitch,pitch,pitch,'George Karumbi')
        print(new_pitch)
        new_pitch.save_pitches()
        return redirect(url_for('timeline',pitch_url = pitch.title ))
    return render_template('pitch.html',pitch = pitch,pitch_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)