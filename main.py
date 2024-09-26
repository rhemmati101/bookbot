def main():
    book_path: str = "books/frankenstein.txt" 
    
    contents = read_file(book_path)
    num_words = wordcount(contents)
    char_counts = character_count(contents)

    print(f"--- Report of {book_path} ---")
    print(f"The document contains {num_words} words")
    for char in char_counts:
        print(f"The {char} character was found {char_counts[char]} times")
    
    return 0

def read_file(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def wordcount(text):
    return len(text.split())

def character_count(text):
    counts = dict()

    for character in text:
        if character.lower() not in counts.keys():
            counts[character.lower()] = 1
        else:
            counts[character.lower()] += 1


    return counts

main()
