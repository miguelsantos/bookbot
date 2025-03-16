def count_words(text):
    word_count = 0

    for w in text.split():
        word_count += 1

    return word_count

def count_characters(text):
    character_numbers = {}
    lowered_text = text.lower()

    for c in lowered_text:
        if c in character_numbers:
            character_numbers[c] += 1
        else:
            character_numbers[c] = 1

    return character_numbers

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    dicts = []

    for k in dict:
        dicts.append({"char": k, "count": dict[k]})

    dicts.sort(reverse=True, key=sort_on)
    return dicts
    
