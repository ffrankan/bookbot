def count_characters(file_contents):
    # only count a-z
    characters_count = {}
    for character in file_contents:
        if not character.isalpha():
            continue
        character = character.lower()
        if character in characters_count:
            characters_count[character] += 1
        else:
            characters_count[character] = 1
    return characters_count

def count_words(file_contents):
    words_count = 0
    for word in file_contents.split():
        words_count += 1
    return words_count

def print_report(book_path, words_count, characters_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    for character in characters_count:
        print(f"The '{character}' character was found {characters_count[character]} times")
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path, "r") as f:
        file_contents = f.read()
        words_count = count_words(file_contents)
        characters_count = count_characters(file_contents)
        print_report(book_path, words_count, characters_count)
main()