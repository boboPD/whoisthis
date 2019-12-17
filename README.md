### SETUP
I am using Python version 3.6.8 for this project. Make sure python and a version of pip compatible with python are installed on the system

#### Installing the Python dependencies
To install dependencies run the following on the root directory of the project
```
pip3 install -r requirements.txt
```

#### Downloading the Stanford NLP Named Entity Recognition tagger
1. Make sure Java runtime is installed on the machine and accessible in the environment. To test that java is properly installed, simply run the following on the command line where you are going to run this project
    ```
    praddas@my-laptop:~/project/whoisthis$ java
    ```
1. Download the Stanford NER binaries from [here](https://nlp.stanford.edu/software/stanford-ner-2018-10-16.zip) and save the zip file in the root folder of the project
1. Extract the contents of the zip file downloaded in the previous step into the root folder of the project. By default the folder name will be `stanford-ner-2018-10-16.zip`. Rename it to `stanford-ner` (just remove the date part of the folder name)

#### Running the code
Just run the following command from the console:
```
praddas@my-laptop:~/project/whoisthis$ python3 whoisthis.py <path to the epub file>
```

**A few sample epub files have been provided on the sample_books folder for testing. These are small childrens books. The named entity recognition step takes a lot of time so don't run it on a large book**

To test on one for the sample books you can run the following:

```
praddas@my-laptop:~/project/whoisthis$ python3 whoisthis.py ./sample_books/tug_of_war.epub
```

### Code Overview
This section provides an overview of all the files and how the code is structured.

[extract_book_contents.py](https://lab.textdata.org/pd10/who-is-this/blob/master/extract_book_contents.py) : This file is responsible for extracting the contents of the epub file and parse the HTML files within it, finally converting all text into a string and returning it.

[character_data.py](https://lab.textdata.org/pd10/who-is-this/blob/master/character_data.py) : This file contains the class `CharacterData` which is essentially a data structure that holds a dictionary that maps from a character's first name to all the lines that the character appears in. It exposes methods for adding names and lines to the structure and fetching that data. It ensures sanity of the data, e.g, names are not repeated and such..

[extract_character_data.py](https://lab.textdata.org/pd10/who-is-this/blob/master/extract_character_data.py) : This file exposes a function `extract_character_names(book_contents)` which takes a string as input and finds all the character names in the string. It then constructs a `CharacterData` object mentioned above by adding the lines for every character. It then returns this object.

[rank_character_actions.py](https://lab.textdata.org/pd10/who-is-this/blob/master/rank_character_actions.py) : This file contains the code that ranks the lines using the [TextRank algorithm](https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/) and then prints out the lines sorted by rank.

[whoisthis.py](https://lab.textdata.org/pd10/who-is-this/blob/master/whoisthis.py) :
This is the main file that is the entry point for our application. It puts all the components together. It first extracts all the content of the book into a string and then passes it to `extract_character_data.extract_character_names(book_contents)`. Once it has the data object that contains all the character names and lines it shows a menu to the user with all the characters listed. Once the user makes a selection it read the lines from the data object and passes them to `rank_character_actions.rank_sentences(lines)`, which ranks and prints the lines.

### Contributors
* Sharanya Paruchuri (sp30)
* Gaurav Bhatt (gauravb2)
* Pradyumna Das (pd10)