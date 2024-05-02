from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import InputRequired, NumberRange


class AddPropertyForm(FlaskForm):
    property_name = StringField('Property Name', validators=[InputRequired()])
    number_of_rooms = IntegerField('No. of Rooms', validators=[InputRequired(), NumberRange(min=0)])
    number_of_bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired(), NumberRange(min=0)])
    location = StringField('Location', validators=[InputRequired()])
    image = FileField('Property Image', validators=[FileAllowed(['jpg', 'png'])])
    price = DecimalField('Property Price', validators=[InputRequired(), NumberRange(min=0)], places=2)
    description = StringField('Description', validators=[InputRequired()])
    type = SelectField(
        'Property Type',
        choices=[('House', 'House'), ('Townhouse', 'Townhouse'), ('Apartment', 'Apartment')],
        default='House',
        validators=[InputRequired()]
    )
    submit = SubmitField('Add Property')
