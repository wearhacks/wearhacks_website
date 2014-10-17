'''
This module defines the fields for the user application forms

'''


from flask_wtf import Form
from wtforms import StringField, RadioField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url

class UserApplication(Form):
    name = StringField('Name', validators=[DataRequired()]) 
    email = StringField('Email', validators=[DataRequired()])
    organization = StringField('Organization', validators=[DataRequired()]) # Could be school or company
    gender =  RadioField('Gender',choices=[('Male', 'male'),('Female', 'female'),('Other', 'other')] ,validators=[DataRequired()])
    first_hackathon = RadioField('First Hackathon',choices=[('Yes', 'yes'),('No', 'no')] ,validators=[DataRequired()])
    github_url = URLField('GitHub', validators=[url()])
    linkedin_url = URLField('LinkedIn', validators=[url()])
    personal_site = URLField('Personal Website', validators=[url()])
    require_travel_reimbursement = RadioField('Travel Reimbursement',choices=[('Yes', 'yes'),('No', 'no')] ,validators=[DataRequired()])
    apply = SubmitField('Apply')
