from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class PostPitch(FlaskForm):
    
    #category = SelectField('Categories', choices = [Category.agritech, Category.cloud,Category.fintech,Category.aiml,Category.block,Category.robotics], default=1)
    pitch = TextAreaField('Tell us your idea!')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    '''
    A class to create a comment form using wtf forms
    '''
    comments = TextAreaField('Leave a comment!')
    submit = SubmitField('Submit')


class CategoryForm(FlaskForm):
    '''
    A class to create categories using wtf forms

    '''

    name = StringField('category name', validators=[Required()])
    submit = SubmitField('Create')