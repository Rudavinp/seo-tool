from flask import render_template, flash, redirect, url_for, session, request, jsonify
from app import app, queue
from app.forms import InputTextForm
import google_app
from markupsafe import Markup
from .utils import handle_form_text
import json



@app.route('/', methods=['GET', 'POST'])
def index():
    # list_to_template = []
    # result_dict = {}
    # text = ''
    # form = InputTextForm()


    # if form.validate_on_submit():

    # if request.method == "POST":
    #     print(5555, request.form['text'])
    #     print(55556, form.text.data)
    #     flash('Your text is being processed - {}'.format(form.text.data))
    #
    #     list_sentences = handle_form_text(form.text.data)
    #     print(1, list_sentences)
    #     job = queue.enqueue(google_app.yandex, list_sentences)
    #     session['key'] = job.id
    #
    #     print(11111111111, session['key'])
    print(4444444, request.method)
    # try:
    #     res = queue.fetch_job(session['key'])
    #     result_dict = res.result
    #     if result_dict:
    #         for k, v in result_dict.items():
    #             if result_dict.get(k):
    #                 list_to_template.append(Markup('<span style="color: #FF6347">{}</span>'.format(k)))
    #             else:
    #                 list_to_template.append(Markup('<span style="color: #00FF00">{}</span>'.format(k)))
    #
    #         text = '.'.join(list_to_template)
    #         text = Markup('<p>{}</p>'.format(text))
    # except Exception as e:
    #     print('yps', e)

    return render_template('index.html')


@app.route('/start', methods=['POST'])
def get_counts():
    data = json.loads(request.data.decode())
    text = data["text"]
    print(32323232, text)
    # flash('Your text is being processed - {}'.format(text))

    list_sentences = handle_form_text(text)
    print(1, list_sentences)
    job = queue.enqueue(google_app.yandex, list_sentences)
    session['key'] = job.id

    print(11111111111, session['key'])
    return job.get_id()


@app.route('/results/<job_key>', methods=['GET'])
def get_results(job_key):
    res = queue.fetch_job(job_key)

    result_dict = res.result
    print(23233, result_dict)
    if result_dict:
        json_dict=[]
        for k, v in result_dict.items():
            d = {}
            d['sentence'] = k
            d['url'] = v[:2]
            json_dict.append(d)
        #     if result_dict.get(k):
        #         list_to_template.append(Markup('<span style="color: #FF6347">{}</span>'.format(k)))
        #     else:
        #         list_to_template.append(Markup('<span style="color: #00FF00">{}</span>'.format(k)))
        #
        # text = '.'.join(list_to_template)
        # text = Markup('<p>{}</p>'.format(text))
        print(444444, json_dict)
        text = jsonify(json_dict)
        print(66666, json_dict)
        return text, 200
    return 'Nay', 202
