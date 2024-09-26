def main():
    book_path: str = "books/frankenstein.txt" 
    
    contents = read_file(book_path)
    # print(contents)
    # print(wordcount(contents))
    print(character_count(contents))
    
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
