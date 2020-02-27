from flask import render_template, flash, redirect, url_for, session
from app import app, queue
from app.forms import InputTextForm
import google_app
from markupsafe import Markup
from .utils import handle_form_text
import os
import redis

import time
from rq import Queue
from redis import Redis



@app.route('/', methods=['GET', 'POST'])
def index():
    list_to_template = []
    result_dict = {}
    text = ''
    form = InputTextForm()


    if form.validate_on_submit():

        flash('Your text is being processed - {}'.format(form.text.data))

        list_sentences = handle_form_text(form.text.data)
        print(1, list_sentences)
        job = queue.enqueue(google_app.yandex, list_sentences)
        session['key'] = job.id

        print(11111111111, session['key'])
    print(4444444)
    try:
        print(23233322)
        res = queue.fetch_job(session['key'])
        result_dict = res.result
        print(23233322)
        if result_dict:
            for k, v in result_dict.items():
                if result_dict.get(k):
                    list_to_template.append(Markup('<span style="color: #FF6347">{}</span>'.format(k)))
                else:
                    list_to_template.append(Markup('<span style="color: #00FF00">{}</span>'.format(k)))

            text = '.'.join(list_to_template)
            text = Markup('<p>{}</p>'.format(text))
    except Exception as e:
        print('yps', e)

    return render_template('index.html', form=form, text=text, list=result_dict)

