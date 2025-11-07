def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            characters[char] = characters.get(char, 0) + 1
    return characters

def sorted_characters(characters):
    list_of_dicts = []
    for char, count in characters.items():
        list_of_dicts.append({"char": char, "num": count})
    list_of_dicts.sort(reverse=True, key=sort_on_num)
    return list_of_dicts

def sort_on_num(item):
    return item["num"]


    