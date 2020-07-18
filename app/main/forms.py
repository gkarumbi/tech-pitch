from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from ..models import Category

class PostPitch(FlaskForm):
    
    #category = SelectField('Categories', choices = [Category.agritech, Category.cloud,Category.fintech,Category.aiml,Category.block,Category.robotics], default=1)
    pitch = TextAreaField('Full Pitch', validators=[Required()])
    submit = SubmitField('Submit')