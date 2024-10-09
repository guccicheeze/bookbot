def main():
    book = "books/frankenstein.txt"
    text = book_text(book)
    word_number = word_count(text)
    char_count = get_character_count(text)
    char_list = get_sorted_char_list(char_count)
    print(f"--- Begin report of {book} ---")
    print(f"{word_number} words found in the document")
    print()
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")

def book_text(book):
    with open(book) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count

def get_sorted_char_list(char_count):
    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list




main()