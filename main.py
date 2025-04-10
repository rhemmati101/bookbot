from stats import *

def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()

    

def main():
    filepath = "./books/frankenstein.txt"

    book_text: str = get_book_text(filepath)
    char_count_list = listify_counts(charcount(book_text))

    #Display
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount(book_text)} total words")
    print("--------- Character Count -------")
    for item in char_count_list:
        if item['name'].isalpha():
            print(f"{item['name']}: {item['count']}")
    print("============= END ===============")

main()
