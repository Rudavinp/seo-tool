import re


def handle_form_text(text, min_len=3, len_for_search=10):
    """
    :param text: text from form
    :param min_len: sentences with this len will be deleted
    :param len_for_search: sentences will be cut to this len
    :return: list processed sentences
    """
    list_sentences = split_text(text)

    good_list_sentences = strip_sens(list_sentences)

    for i in range(len(good_list_sentences)):
        if not good_list_sentences[i] or len(good_list_sentences[i]) < min_len:
            good_list_sentences.remove(good_list_sentences[i])

    for i in range(len(good_list_sentences)):
        if len(good_list_sentences[i].split()) > len_for_search:
            good_list_sentences[i] = ' '.join(good_list_sentences[i].split()[:len_for_search])

    return good_list_sentences


def split_text(text):
    list_sentences = re.split(r'[\.;]+', text)
    return list_sentences


def strip_sens(list_sens):
    good_list_sentences = list(map(lambda x: x.strip(), list_sens))
    return good_list_sentences