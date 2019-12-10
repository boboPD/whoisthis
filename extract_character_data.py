from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.tag.stanford import StanfordNERTagger

from character_data import CharacterData

def extract_character_names(book_contents):
    data = CharacterData()

    lines = sent_tokenize(book_contents)
    tagger = StanfordNERTagger("./stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz", "./stanford-ner/stanford-ner.jar")

    discovered_names_in_line = set()
    for line in lines:
        words = word_tokenize(line)
        taggd_token = tagger.tag(words)

        name = ""
        first_name = ""
        discovered_names_in_line.clear()
        for word, tag in taggd_token:
            if tag == "PERSON":
                if name == "":
                    first_name = word
                name += word + " "
            else:
                if name != "":
                    name = name.strip()
                    if first_name not in discovered_names_in_line:
                        data.add_line_for_name(first_name, name, line)
                        discovered_names_in_line.add(first_name)
                    name = ""
                    first_name = ""

    return data
