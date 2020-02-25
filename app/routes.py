from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import InputTextForm
import google_app
from markupsafe import Markup
import os
import redis

import time
from rq import Queue
from redis import Redis

# redis_conn = Redis()
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)

queue = Queue(connection=conn)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_dict = []
    list_matches = []
    list_to_template = []
    form = InputTextForm()
    text_ = "Text"
    jobs =  queue.jobs
    print(5454545, jobs)
    text = Markup('<span style="color: #fa8e47">{}</span>'.format(text_))

    if form.validate_on_submit():

        list_matches = {}
        flash('Your text is being processed - {}'.format(form.text.data))
        list_sentences = form.text.data.split('.')

        # print(8, list_sentences)

        list_sentences = list(map(lambda x: x.strip(), list_sentences))
        # print(88, list_sentences)

        for i in range(len(list_sentences)):
            if not list_sentences[i] or len(list_sentences[i]) < 3:
                list_sentences.remove(list_sentences[i])



        # print(888, list_sentences)
        for i in range(len(list_sentences)):
            if len(list_sentences[i].split()) > 10:
                list_sentences[i] = ' '.join(list_sentences[i].split()[:10])
        # print(888888, list_sentences)



        job = queue.enqueue(google_app.yandex, list_sentences)
        session['key'] = job.id

        # result_dict = job.result

        print(11111111111)

        # for sen in list_sentences:
        #     # time.sleep(3)
        #     result = yandex(sen)
        #     if result:
        #         list_matches[sen] = result
        #     else:
        #         list_matches[sen] = []
    try:
        res = queue.fetch_job(session['key'])

        result_dict = res.result
        print(4444444, result_dict)
        if result_dict:
            for k, v in result_dict.items():
                if result_dict.get(k):
                    # print(22)
                    list_to_template.append(Markup('<span style="color: #FF6347">{}</span>'.format(k)))
                else:
                    list_to_template.append(Markup('<span style="color: #00FF00">{}</span>'.format(k)))

            text = '.'.join(list_to_template)
            text = Markup('<p>{}</p>'.format(text))
        # print(12, result_dict)
    except Exception as e:
        print('yps', e)



        # return redirect(url_for('index', text=text))
        # return render_template('index.html', form=form, text=text, list=result_dict)


    return render_template('index.html', form=form, text=text, list=result_dict)

