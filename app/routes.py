from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InputTextForm
from google_app import yandex
from markupsafe import Markup

import time
from rq import Queue
from redis import Redis

def like_route(result_dict):

    return render_template('index.html', list=result_dict)

@app.route('/', methods=['GET', 'POST'])
def index():
    list_matches = []
    form = InputTextForm()
    text_ = "Text"
    text = Markup('<span style="color: #fa8e47">{}</span>'.format(text_))

    if form.validate_on_submit():
        list_to_template = []
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

        redis_conn = Redis()
        queue = Queue(connection=redis_conn)

        job = queue.enqueue(yandex, list_sentences)
        print(job.result)
        # time.sleep(60)
        print(job.result)
        result_dict = job.result

        print(11111111111)

        # for sen in list_sentences:
        #     # time.sleep(3)
        #     result = yandex(sen)
        #     if result:
        #         list_matches[sen] = result
        #     else:
        #         list_matches[sen] = []
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




        # return redirect(url_for('index', text=text))
        return render_template('index.html', form=form, text=text, list=result_dict)
    return render_template('index.html', form=form, text=text, list=None)
