def is_number(s):
    try:
        float(s)  # for int, long and float
    except ValueError:
        try:
            complex(s)  # for complex
        except ValueError:
            return False
    return True


def remove_end_symbol(text):
    if text.endswith('.') or text.endswith(',') or text.endswith('?'):
        text = text[:-1]

    if text.endswith('%'):
        print(text)
        text = text[:-1]
        dot_index = text.find('.')
        if dot_index == 0:
            text = "0.00" + text[dot_index + 1:]
        elif dot_index == 1:
            text = "0.0" + text[:dot_index] + text[dot_index + 1:]
        elif dot_index == 2:
            text = "0." + text[dot_index - 2:dot_index] + text[dot_index + 1:]
        elif dot_index > 2:
            text = text[:dot_index - 2] + "." + text[dot_index - 2:dot_index] + text[dot_index + 1:]
        else:
            text = "0.0" + text
        print(text)

    return text

text='45%'

remove_end_symbol(text)