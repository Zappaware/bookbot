import sys
from stats import count_words, count_characters, sort_dict



def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    num_arg = len(sys.argv)
    if num_arg == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        word_count_in_text = count_words(get_book_text(sys.argv[1]))
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...") 
        print("----------- Word Count ----------")
        print(f"Found {word_count_in_text} total words")
        print("--------- Character Count -------")
        char_count_in_text = sort_dict(count_characters(get_book_text(sys.argv[1])))
        print("============= END ===============""")

main()


