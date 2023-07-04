import os
from flask import render_template, request, flash, redirect, url_for
from .forms import HiveForm, WeatherForm
from .import bp as main
from flask_login import login_required, current_user
from app.models import User, Hive, Apiary
import requests


@main.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')

@main.route('/hive', methods=['GET', 'POST'])
@login_required
def hive():
    form = HiveForm()
    if request.method == 'POST':
        
        new_hive_data={
            "hive_name" : form.hive_name.data,
            "numOfDeeps" : form.numOfDeeps.data,
            "numOfMediums" : form.numOfMediums.data,
            "numOfShallows" : form.numOfShallows.data,
            "queen" : form.queen.data,
            "health" : form.health.data,
            "temperment" : form.temperment.data,
            "notes" : form.notes.data
        }

        new_hive_object = Hive()
        new_hive_object.hive_from_dict(new_hive_data)
        new_hive_object.save()

        new_apiary_hive = Apiary()
        new_apiary_hive.user_id=current_user.id
        new_apiary_hive.hive_id=new_hive_object.hive_id
        my_hives=Apiary.query.filter_by(user_id=current_user.id).all()

        hives=''
        my_hive_names=[]
        hive_list=[]
        for entry in my_hives:
            h=Hive.query.filter_by(hive_id=entry.hive_id).first().hive_name
            my_hive_names.append(h)

        if new_hive_object.hive_name in my_hive_names:
            flash(f'You already have a hive by this name/id.  Please choose another.', 'danger')
        else:
            flash(f'Hive information saved.', 'success')
            current_user.add_hive(new_hive_object)

        hives = current_user.hive.all()
        hive_list = hives

        return render_template('hive.html.j2', hives=hive_list, form=form)
    return render_template('hive.html.j2', form=form)

@main.route('/apiary', methods=['GET', 'POST'])
@login_required
def apiary():
    hives = current_user.hive.all()
    hive_list=hives
    return render_template('apiary.html.j2', hives=hive_list)

@main.route('/weather', methods=['GET', 'POST'])
@login_required
def weather():
    form=WeatherForm()
    forecast_dict={}
    if request.method == 'POST' and form.validate_on_submit():
        zip = form.zip.data
        api = os.environ.get('API_SECRET')
        url = f'https://api.openweathermap.org/data/2.5/weather?zip={zip}&appid={api}&units=imperial'
        response=requests.get(url)
        forecast=response.json()
        print(forecast)
        forecast_dict={
            "temp": forecast["main"]["temp"],
            "weather": forecast["weather"][0]["main"]         
        }
        print(forecast_dict)
        return render_template('weather.html.j2', form=form, forecast=forecast_dict)

    forecast=[]
    return render_template('weather.html.j2', form=form, forecast=forecast_dict)


@main.route('/remove_hive/<int:id>')
@login_required
def remove_hive(id):
    h=Hive.query.filter_by(hive_id=id).first()
    current_user.remove_hive(h)
    return redirect(url_for('main.apiary'))


