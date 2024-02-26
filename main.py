def main():
    path = "./books/frankenstein.txt"
    text = read_text_from_file(path)
    word_count = get_word_count(text)

def read_text_from_file(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())
