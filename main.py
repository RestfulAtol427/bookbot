import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    characters = {}
    total_chars = get_num_char(text,characters)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in the document")
    print("")
    for char in total_chars:
        amt = total_chars[char]
        print(f"The '{char}' character was found {amt} times")



def get_num_char(text,characters):
    amt = 1
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            if char in characters:
                characters[char] = (characters[char]) + 1
            else:
                characters[char] = amt
    return characters

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()