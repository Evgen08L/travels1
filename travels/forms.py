from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class TravelForm(FlaskForm):
    destination = StringField('Destination', validators=[DataRequired()])
    start_date = StringField('Start Date', validators=[DataRequired()])
    end_date = StringField('End Date', validators=[DataRequired()])
    budget = IntegerField('Budget', validators=[DataRequired()])
    services = StringField('Services')
    submit = SubmitField('Submit')