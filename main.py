file_path = "books/frankenstein.txt"

def get_book_text(file_path):
    with open(file_path) as file:
        file_text = file.read()
    return file_text

def get_word_count(file_text):
    words = file_text.split()
    words = len(words)
    print (f"Found {words} total words")

def main():
    book_text = get_book_text(file_path)
    get_word_count(book_text)

main()