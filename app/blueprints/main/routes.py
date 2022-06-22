from flask import render_template, request, flash, redirect, url_for
import requests
from .forms import HiveForm
from .import bp as main
from flask_login import login_required, current_user
from app.models import User, Hive
import random

@main.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')

@main.route('/hive', methods=['GET', 'POST'])
@login_required
def hive():
    form = HiveForm()
    if request.method == 'POST' and form.validate_on_submit:
        try:
            new_hive_data={
                "name" : form.name.data,
                "queen" : form.queen.data,
                "health" : form.health.data,
                "temperment" : form.temperment.data,
                "notes" : form.notes.data
            }

            new_hive_object = Hive()
            new_hive_object.from_dict(new_hive_data)
            new_hive_object.save()

        except:
            flash("There was an unexpected error saving your hive information. Please try again later.", "danger")
            return render_template('hive.html.j2', form=form)
        flash('Hive information saved.', 'success')
        return redirect(url_for('main.index'))
    return render_template('hive.html.j2', form=form)
