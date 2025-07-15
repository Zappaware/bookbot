def count_words(text):
    splited_text = text.split()
    count = 0
    for i in range(0,len(splited_text)):
        count += 1
    return count

def count_characters(text):
    lowercase_text = text.lower()
    count = {}

    for character in lowercase_text:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    return count

def sort_dict(dictionary):
    sorted_items = sorted(dictionary.items())
    new_dict = dict(sorted_items)
    for key, value in new_dict.items():
        if key.isalpha():
            print(f"{key}: {value}")


