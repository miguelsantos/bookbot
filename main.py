import sys
from stats import count_words, count_characters, sort_dict

def get_book_text(path):
    file_contents = ""

    with open(path) as f:
        file_contents = f.read()    

    return file_contents


def main():
    # book_text = get_book_text("./books/frankenstein.txt")
    
    num_words = count_words(book_text)

    num_characters = count_characters(book_text)

    sorted_list = sort_dict(num_characters)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count in sorted_list:
        if count["char"].isalpha():
            print(f"{count["char"]}: {count["count"]}")

    print("============= END ===============")

main()
