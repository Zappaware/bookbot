from stats import count_words, count_characters, sort_dict

path = "/home/sergi/bookbot/books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    word_count_in_text = count_words(get_book_text(path))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...") 
    print("----------- Word Count ----------")
    print(f"Found {word_count_in_text} total words")
    print("--------- Character Count -------")
    char_count_in_text = sort_dict(count_characters(get_book_text(path)))
    print("============= END ===============""")

main()


