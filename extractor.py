import sys
from bs4 import BeautifulSoup
import lxml
import re
import os

if len(sys.argv) != 2:
    print("please provide the path to the epub contents")

spine_xml = ""
with open(f"{sys.argv[1]}/content.opf", "r", encoding="utf8") as spine_file:
    spine_xml = spine_file.read()
    
spine_contents = BeautifulSoup(spine_xml, "lxml-xml")
manifest_contents = spine_contents.find("manifest")

html_page_list = []
for ref in spine_contents.find("spine").find_all("itemref"):
    manifest_item = manifest_contents.find("item", id=ref["idref"])
    html_page_list.append(manifest_item["href"])


print(f"Found {len(html_page_list)} html files in epub")

book_contents = ""
for content_file in html_page_list:
    print(f"Processing file: {content_file}")
    with open(f"{sys.argv[1]}/{content_file}", "r", encoding="utf8") as filereader:
        soup = BeautifulSoup(filereader.read(), "lxml")
        body = soup.find("body")
        
        for item in body.stripped_strings:
            book_contents += item

print("Writing complete contents to output file")

if not os.path.exists("./output"):
    os.makedirs("./output")
with open("./output/book.txt", "w", encoding="utf8") as output:
    output.write(book_contents)