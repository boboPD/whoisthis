from bs4 import BeautifulSoup
import lxml
import os

def extract_book_content(path):
    spine_xml = ""
    with open(f"{path}/content.opf", "r", encoding="utf8") as spine_file:
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
        #print(f"Processing file: {content_file}")
        with open(f"{path}/{content_file}", "r") as filereader:
            soup = BeautifulSoup(filereader.read(), "lxml")
            body = soup.find("body")
            
            for item in body.stripped_strings:
                book_contents += item

    return book_contents