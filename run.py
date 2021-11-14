from statistics.Statistics import Statistics
from statistics.actions_on_files import all_file_words


def run():
    file = Statistics.open_file("dickens.txt")
    data = file.read()
    file.seek(0)
    all_words = all_file_words(file)
    file.seek(0)
    choice = 8
    while choice is not 0:
        choice = input("""Welcome to Statistics Actions On Text File
        Enter 1 for amount of lines 
        Enter 2 for amount of words
        Enter 3 for amount of unique words
        Enter 4 for max and average sentence lengths
        Enter 5 for most popular word with no syntactic meaning 
        Enter 6 for the longest subsequnce without 'k' 
        Enter 7 for amount of colors occurences
        Enter 0 to end
        """)
        choice = int(choice) if choice.isdigit() else -1
        res =''
        if choice is 0:
            file.close()
            print("Goodbye")
        elif choice is 1:
            res = Statistics.count_lines(file)
            print("Number of lines in file: ", res)
        elif choice is 2:
            res = Statistics.count_words(all_words)
            print("Number of words in file: ", res)
        elif choice is 3:
            res = Statistics.count_unique_words(all_words)
            print("Number of unique words in file: ", res)
        elif choice is 4:
            res = Statistics.max_and_avg_sentence_length(data)
            print(f"""
            Max sentence length: {res[0]}
            Average sentence length: {res[1]}
            """)
        elif choice is 5:
            res = Statistics.most_popular_word(all_words)
            print("Most Popular word in the text: ", res)
        elif choice is 6:
            res = Statistics.longest_subsequnce_without_k(all_words)
            print("The longest subsequence without a 'k': ", res)
        elif choice is 7:
            res = Statistics.colors_appearances(data)
            print("Colors that appears in the text and no. of apearences: ")
            for color, amount in res:
                print(color, ":", amount)
        else:
            print("Unrecognized action no., please try again")
   
   

if __name__ == '__main__':
    run()