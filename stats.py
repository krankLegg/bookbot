def get_num_words(text):
    t = text.split()
    return len(t)

def get_num_characters(text):
    text = text.lower()
    characters = {}

    for key in text:
        if key in characters:
            count = characters[key] + 1
            characters.update({key: count})
        else:
            characters[key] = 1

    return characters

def get_sorted_list(text):
    return dict(sorted(text.items()))
