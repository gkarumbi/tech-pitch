from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField,SubmitField,SelectField
from wtform.validators import Required

class PostPitch(FlaskForm):
    category = SelectField('Categories', choices = dropdown_list, default=1)
    pitch = TextAreaField('Full Pitch', validators=[Required()])
    submit = SubmitField('Submit')