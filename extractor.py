import sys
from bs4 import BeautifulSoup
import lxml
import re
import os

if len(sys.argv) != 2:
    print("please provide the path to the epub contents")
    
#Changing the working directory to the folder containing the epub contents so that relative pathing works easily
os.chdir(sys.argv[1])

spine_xml = ""
toc_xml = ""
with open("content.opf", "r", encoding="utf8") as spine_file:
    spine_xml = spine_file.read()
with open("toc.ncx", "r", encoding="utf8") as toc_file:
    toc_xml = toc_file.read()
    
spine_contents = BeautifulSoup(spine_xml, "lxml-xml")
toc_contents = BeautifulSoup(toc_xml, "lxml-xml")
html_page_list = [x["href"] for x in spine_contents.find_all("item", href=re.compile("html$"))]

print(f"Found {len(html_page_list)} html files in epub")

book_contents = ""
for content_file in html_page_list:
    print(f"Processing file: {content_file}")
    with open(content_file, "r", encoding="utf8") as filereader:
        soup = BeautifulSoup(filereader.read(), "lxml")
        body = soup.find("body")
        
        for item in body.stripped_strings:
            book_contents += item

print("Writing complete contents to output file")
with open("output.txt", "w", encoding="utf8") as output:
    output.write(book_contents)