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