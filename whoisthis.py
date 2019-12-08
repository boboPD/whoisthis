import extract_book_contents
import extract_character_data
import os
from rank_character_actions import rank_sentences

def create_character_to_input_map(list_of_names):
    map = {}
    for i, name in enumerate(list_of_names):
        map[i+1] = name

    return map

def display_choices(number_to_char_map):
    print("CHARACTERS IN THE BOOK:")
    for number, name in number_to_char_map.items():
        print(f"{number}. => {name}\n")

if not os.path.isdir("./output"):
    os.mkdir("./output")

book_as_text = extract_book_contents.extract_book_content("./sample_books/tug_of_war")
with open("./output/book.txt", "w", encoding="utf8") as output:
    output.write(book_as_text)

character_and_sentences = extract_character_data.extract_character_names(book_as_text)

input_to_char_map = create_character_to_input_map(character_and_sentences.get_all_character_names())
number_of_characters = len(input_to_char_map.keys())

user_input = 1
while user_input > 0:
    print("========================================================")

    display_choices(input_to_char_map)
    user_input = eval(input("Please enter the number corresponding to the character you want to choose (-1 to exit): "))

    if user_input > number_of_characters or user_input < 0:
        message = "Invalid user input" if user_input > number_of_characters else "Exiting..."
        print(message)
        continue

    lines = character_and_sentences.get_lines_for_character(input_to_char_map[user_input])
    rank_sentences(lines)

    print("========================================================")


