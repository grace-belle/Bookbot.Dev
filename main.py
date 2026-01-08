from stats import get_word_count, get_character_count, sorted_report
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_text = file.read()
    return file_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    get_word_count(book_text)
    sorted_report(get_character_count(book_text))

main()