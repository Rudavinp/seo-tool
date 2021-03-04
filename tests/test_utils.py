from app import utils


def test_handle_text():
    text = ['abc',
            'i will find good idea']
    handle_sens = utils.handle_form_text(text)

    assert isinstance(handle_sens, list)
    assert len(handle_sens) == 1


def test_re_split():
    texts = (' abc ;' \
           'bbb;', '')
    for t in texts:
        list_sens = utils.split_text(t)
        print(list_sens)
        assert isinstance(list_sens, list)


def test_strip_sents():
    list_sens = ['  avc ',
                 '      ff ff   ']
    good_list = utils.strip_sens(list_sens)
    print(12, good_list)
    assert isinstance(good_list, list)
    assert not good_list[1].startswith(' ')
    assert not good_list[1].endswith(' ')
    assert ' ' in good_list[1]


