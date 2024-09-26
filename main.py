def main():
    book_path: str = "books/frankenstein.txt" 
    
    contents = read_file(book_path)
    num_words = wordcount(contents)
    char_counts_dict = character_count(contents)

    # convert char_counts dict to list of dicts with char and count keys for each char
    char_counts_list = dict_to_list(char_counts_dict)

    # sort char_counts to be printed in order of most common to least common char
    char_counts_list.sort(reverse=True, key=lambda dict: dict["count"])

    print_report(book_path, num_words, char_counts_list)
    
    return 0

def read_file(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def wordcount(text):
    return len(text.split())

# only tallies alphabetic chars
def character_count(text):
    counts = dict()

    for char in text:
        if not char.isalpha():
            continue
        if char.lower() not in counts.keys():
            counts[char.lower()] = 1
        else:
            counts[char.lower()] += 1


    return counts

def print_report(book_path, num_words, char_counts_list):
    print(f"--- Report of {book_path} ---")
    print(f"The document contains {num_words} words")
    for char_dict in char_counts_list:
        print(f"The {char_dict['char']} character was found {char_dict['count']} times")

def dict_to_list(char_counts_dict):
    char_counts_list = []
    for char in char_counts_dict:
        ith_dict = {}
        ith_dict["char"] = char
        ith_dict["count"] = char_counts_dict[char]
        
        char_counts_list.append(ith_dict)

    return char_counts_list

main()
