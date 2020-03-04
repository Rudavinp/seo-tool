import re

def handle_form_text(text):
    list_sentences = re.split(r'[\.;]+', text)

    list_sentences = list(map(lambda x: x.strip(), list_sentences))

    for i in range(len(list_sentences)):
        if not list_sentences[i] or len(list_sentences[i]) < 3:
            list_sentences.remove(list_sentences[i])

    for i in range(len(list_sentences)):
        if len(list_sentences[i].split()) > 10:
            list_sentences[i] = ' '.join(list_sentences[i].split()[:10])

    return list_sentences