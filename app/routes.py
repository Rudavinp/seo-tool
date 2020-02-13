from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InputTextForm
from google_app import yandex

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputTextForm()
    if form.validate_on_submit():
        flash('Your text is being processed - {}'.format(form.text.data))
        print(1, type(form.text.data))
        print(2, len(form.text.data))
        yandex(form.text.data)

        return redirect(url_for('index'))
    return render_template('index.html', form=form)
