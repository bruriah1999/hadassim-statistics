from enum import unique
import re
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from statistics.actions_on_files import split_into_sentences
from statistics.constants import COLORS, SYNTACTIC_TAGS
nltk.download('punkt')
nltk.download('pos_tag')

class Statistics:

    @staticmethod
    def open_file(filename_path):
        """Recieve a file path and reads it for statistics calculations."""

        return open(filename_path, "r", encoding="utf8")

    @staticmethod
    def count_lines(file):
        """Count the number of lines in the file."""

        lines_counter = 0
        for line in file:
            if line != "\n":
                lines_counter += 1
        file.seek(0)
        return lines_counter


    @staticmethod
    def count_words(all_words):
        """Count the number of words in the file.

        Uses a helper function that extracts the file's words using Regex
        for a more accurate results
        """

        words_count = len(all_words)
        return int(words_count)


    @staticmethod
    def count_unique_words(all_words):
        """Count the number of unique words in the file.

        Uses a helper function that extracts the file's words using Regex
        for a more accurate results.
        Once having all file's words, the method insert the words into
        a set data structure, which can only contain a word once, then 
        returns the size of the set.
        """

        unique_words = set()
        for word in all_words:
            unique_words.add(word)
        return len(unique_words)


    @staticmethod
    def max_and_avg_sentence_length(data):
        """Calculate the maximal and the average sentence lengths.

        Uses a helper function that extracts the file's sentences using Regex
        for a more accurate results.
        Once having all file's sentences, the method loops through each sentence
        and does the following:
        1. Compares the current sentence length with the maximum length so far
        2. Sums up the length of the current sentence into a variable
        Once done, we are left with the maximal sentence length, and devide
        the sum of all sentences length by the number of sentences in-order to
        get the avarage length.
        """

        sentences = split_into_sentences(data)
        max_len = sum_of_lengths = 0.
        for line in sentences:
            curr_line_length = len(line)
            if(curr_line_length > max_len):
                max_len = curr_line_length
            sum_of_lengths += curr_line_length
        return (max_len, int(sum_of_lengths/(len(sentences)-1)))


    @staticmethod
    def most_popular_word(all_words):
        """Find the most popular word in the text which doesn't 
        have a syntactic meaning in English.

        This method is using an external library called 'nltk'
        NLTK provides a service called pos_tag, given a word, it tells us 
        what 'group' of english words the word belongs to.
        In-order to find the most popular word, the method counts the number
        of appearances of each word in the text file which doesn't have a 
        syntactic meaning.
        It uses the dictionary data structure for counting, which saves up in
        running time. it takes O(1) time to add count to a key. at the end it will
        return the key, the word, with the largest number of appearances.
        """

        text = ' '.join(all_words)
        data_dict_without_sw = dict()
        most_popular = ''
        cnt_most_popular = 0

        for word in all_words:
            tag = pos_tag(word_tokenize(word.lower()))
            if len(word)>1 and tag[0][1] not in SYNTACTIC_TAGS:
                if word in data_dict_without_sw:
                    data_dict_without_sw[word] = data_dict_without_sw[word] + 1
                else:
                    data_dict_without_sw[word] = 1
                if data_dict_without_sw[word] > cnt_most_popular:
                    cnt_most_popular = data_dict_without_sw[word]
                    most_popular = word
        return most_popular


    @staticmethod
    def longest_subsequnce_without_k(all_words):
        """Find the longest subsequence without the char 'K' / 'k'
        
        The method is using two pointers and goes linearly over the text file 
        words as follows:
        Initially it finds the first word's position that contains a 'k'.
        Then, finds the next word's position, starting from the last found, 
        that as well contains the char 'k'.
        Once found, the method calculates the size of the gap between the tow
        positions and compares it with the largest gap length found so far.
        
        The while loop doesn't handle two edge cases of when the longest 
        subsequence is at the begining or at the end of the text.
        Those are taken care of separately.
        """

        max_ss_len = start = end = curr_len = 0
        
        while start < int(len(all_words)) and all_words[start].find(fr"[k-kK-K]")!=-1:
            start+=1
        max_ss_len = start
        end=start+1
        

        while end < len(all_words):
            if all_words[end].find('k')==-1 and all_words[end].find('K')==-1:
                end+=1
                curr_len+=1
            else:
                if curr_len > max_ss_len:
                    max_ss_len = curr_len
                    subseq = all_words[start:end]
                curr_len = 0
                start = end+1
                while start < len(all_words) and all_words[start].find(fr"[k-kK-K]")!=-1:
                    start+=1
                end=start+1

        if curr_len > max_ss_len:
            max_ss_len = curr_len

        return int(max_ss_len)
    

    @staticmethod
    def colors_appearances(data):
        """Find colors that appear in the text and their appearances amount.

        The method is using a constant list of 11 basic colors to look for 
        in the text.
        It uses the Regex 'findall' method which is similar to 'count' method 
        in-order to find each color appearances.
        The regular expression used for the color, prevents the method from 
        mistakenly considering a word that only contains the name of the color
        as an appearence of the color itself. for ex., 'predict' -> red.
        """
        
        color_appearance = list()
        for color in COLORS:
            cnt = len(re.findall(fr"[^a-zA-Z][{color[0]}{color[0].lower()}]{color[1:]}[^[a-zA-Z]", data))
            if cnt > 0:
                color_appearance.append((color, cnt))
        return color_appearance
