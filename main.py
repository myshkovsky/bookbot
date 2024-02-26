def main():
    path = "./books/frankenstein.txt"
    text = read_text_from_file(path)
    word_count = get_word_count(text)
    char_dict = get_char_dict(text)
    sorted_dict = sort_dict_by_value(char_dict)


def read_text_from_file(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    return len(text.split())


def get_char_dict(text):
    chars_dict = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        chars_dict[char] = chars_dict.get(char, 0) + 1
    return chars_dict


def sort_dict_by_value(x):
    return dict(sorted(x.items(), key=lambda item: item[1], reverse=True))


main()
