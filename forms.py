from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField('Pet Name', validators=[
                       InputRequired(message='Pet name cant be blank!')])

    # species = StringField('Species', validators=[
    #     InputRequired(message='Species cant be blank!'),
    #     AnyOf(['cat', 'dog', 'porcupine'], message='Species must be either cat, dog, or porcupine')]

    species = StringField('Species', validators=[
        InputRequired(message='Species cant be blank!'),
        AnyOf(['cat', 'dog', 'porcupine'], message='Species must be either cat, dog, or porcupine')])
    photo_url = StringField('Photo URL', validators=[
        InputRequired(message='Photo URL cant be blank!')])
    age = IntegerField('Age', validators=[
        InputRequired(message='Please enter a valid number')])
    notes = StringField('Pet Notes')
