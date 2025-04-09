def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()
    
def wordcount(text: str) -> int:
    return len(text.split())

def main():
    frankenstein_text: str = get_book_text("./books/frankenstein.txt")
    print(f"{wordcount(frankenstein_text)} words found in the document")

main()
