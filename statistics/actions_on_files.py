import re
from string import whitespace, punctuation
from statistics.constants import ALPHABETS, PREFIXES, SUFFIXES, STARTERS, ACRONYMS


def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(PREFIXES,"\\1<prd>",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + ALPHABETS + "[.] "," \\1<prd> ",text)
    text = re.sub(ACRONYMS+" "+STARTERS,"\\1<stop> \\2",text)
    text = re.sub(ALPHABETS + "[.]" + ALPHABETS + "[.]" + ALPHABETS + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(ALPHABETS + "[.]" + ALPHABETS + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+ALPHABETS+"[.] "+STARTERS," \\1<stop> \\2",text)
    text = re.sub(" "+SUFFIXES+"[.]"," \\1<prd>",text)
    text = re.sub(" " + ALPHABETS + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

def all_file_words(file):
    all_words = list()
    for line in file:
        line = line.strip("\n")
        words = re.split('; |,|, | ', line)
        for word in words:
            x = word.strip(whitespace + punctuation)
            if len(x)>0 and x not in punctuation:
                all_words.append(x)
    return all_words
