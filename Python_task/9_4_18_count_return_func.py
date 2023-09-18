def remove_marks(text, marks):
    remove_marks.count = remove_marks.__dict__.get('count', 0) + 1
    return ''.join(filter(lambda x: x not in marks, text))