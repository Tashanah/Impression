from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title  = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie Review', validators=[Required()])
    submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators = [Required ()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField("Pitch Title",validators=[Required()])
    pitch = TextAreaField('Write your pitch here')
    category = SelectField("Pitch category",choices=[('Pickup Lines', 'Pickup Lines'),('Interview pitch', 'Interview pitch'),('Product pitch', 'Product pitch')],validators=[Required()])
    submit = SubmitField('Submit')
    