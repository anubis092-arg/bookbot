import sys
from stats import count_words, count_characters, sorted_characters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        return file_content
        
text = get_book_text(book_path)
word_count = count_words(text)
characters = count_characters(text)
sorted_dict = sorted_characters(characters)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")
print("============= END ===============")