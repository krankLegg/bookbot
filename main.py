import sys
from stats import get_num_words, get_num_characters, get_sorted_list


if len(sys.argv) >= 2:
    filepath = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text = get_book_text(filepath)
    word_count = get_num_words(text)
    characters = get_num_characters(text)
    sorted_characters = get_sorted_list(characters)


    print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")

    for character in sorted_characters:
        if character.isalpha():
            print(f"{character}: {sorted_characters[character]}")
    print("============= END ===============")

main()