import os
from shutil import rmtree, copy
from zipfile import ZipFile

def create_character_to_input_map(list_of_names):
    map = {}
    for i, name in enumerate(list_of_names):
        map[i+1] = name

    return map

def display_choices(number_to_char_map):
    print("CHARACTERS IN THE BOOK:")
    for number, name in number_to_char_map.items():
        print(f"{number}. => {name}\n")

def extract_contents_and_process_epub(filepath):
    wd = "./output/epubcontents"
    rmtree("./output")
    os.makedirs(wd)

    print("Copying epub to working dir...")
    copy(filepath, "./output/epub.zip")

    print("Extracting epub contents...")
    with ZipFile("./output/epub.zip", "r") as zipref:
        zipref.extractall(wd)
    
    print("Looking for content.opf...")
    for root, dirs, files in os.walk(wd):
        if "content.opf" in files:
            return root
    
    raise ValueError("Ebook does not contain a content.opf file")