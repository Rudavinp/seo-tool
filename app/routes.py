from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InputTextForm
from google_app import yandex
from markupsafe import Markup
import time

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputTextForm()
    text_ = "Text"
    text = Markup('<span style="color: #fa8e47">{}</span>'.format(text_))
    # text = Markup('<p>{}</p>'.format(str('<span style="color: #fa8e47">У людей было много видов, до наших дней дожил только один – современный человек разумный</span>.<span style="color: #fa8e47"> Много ветвей человечества оказались тупиковыми и вымерли в результате природных катаклизмов, войн и эволюции</span>.<span style="color: #fa8e47"> О восьми представителях людского рода, ведущих свою историю 2,8 млн лет – в нашем материале</span>.<span style="color: #fa8e47"></span>')))

    if form.validate_on_submit():
        list_to_template = []
        list_matches = {}
        flash('Your text is being processed - {}'.format(form.text.data))
        list_sentences = form.text.data.split('.')

        for sen in list_sentences:
            time.sleep(2)
            result = yandex(sen)
            print(1, result)
            if result:
                list_matches[sen] = result
            else:
                list_matches[sen] = []

        for k, v in list_matches.items():
            if list_matches.get(k):
                print(22)
                list_to_template.append(Markup('<span style="color: #FF6347">{}</span>'.format(k)))
            else:
                list_to_template.append(Markup('<span style="color: #00FF00">{}</span>'.format(k)))

        text = '.'.join(list_to_template)
        text = Markup('<p>{}</p>'.format(text))
        print(12, list_sentences)
        print(12, text)
        # snippets = yandex(form.text.data)


        # return redirect(url_for('index', text=text))
        return render_template('index.html', form=form, text=text)
    return render_template('index.html', form=form, text=text)
