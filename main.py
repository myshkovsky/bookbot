def main():
    path = "./books/frankenstein.txt"
    text = read_text_from_file(path)

def read_text_from_file(path):
    with open(path) as f:
        return f.read()
