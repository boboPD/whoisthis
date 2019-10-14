### SETUP
I am using Python version 3.6.8 for this project. Make sure python and a version of pip compatible with python are installed on the system

To install dependencies run the following on the root directory of the project
```
pip install -r requirements.txt
```

#### Extracting the contents from an EPUB file
The extractor.py script extracts the contents from an EPUB file and writes them out into a plain text file.
1. Change the extension of the EPUB file from .epub to .zip
1. Extract the content of the zip file
1. Inside the extracted folder find the path to the `content.opf` and `toc.ncx`. These files should be in the same folder. Use the books in the sample_books folder as a guide.
1. Run `python extractor.py <path to the folder containing the content.opf file>`
1. This will generate the plaintext file in the following location: `./output/book.txt`

Sample:
```
python extractor.py ./sample_books/tug_of_war
python extractor.py ./sample_books/David_Copperfield_by_Charles_Dickens/OEBPS
```