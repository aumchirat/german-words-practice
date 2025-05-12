import pandas as pd
import random
import time

nouns_df = pd.read_excel("./data/most-used-german-words.xlsx", sheet_name='nouns')
# noun_data = nouns_df.set_index('german')['english'].to_dict()
noun_data = nouns_df.to_dict('records')
# any english definition with "|"


def practice_nouns(practice_set=noun_data):
    print("How many words would you like to practice? (from 1 to " + str(len(practice_set)) + ")")
    num_words = input()
    pracetice_words = []
    # random key and value
    for i in range(int(num_words)):
        random_num = random.randint(0, len(practice_set) - 1)
        ger = practice_set[random_num]["german"]
        eng_list = practice_set[random_num]["english"].split("|")
        print(ger + ": ")
        answer = input()
        if answer in eng_list:
            print('CORRECT!')
        else:
            print('That is not correct, the correct answer is ' + practice_set[random_num]["english"])
            pracetice_words.append(practice_set[random_num])
    # if there're still words to learn
    if len(pracetice_words) > 0:
        print("words you don't know: ")
        for word in pracetice_words:
            print(word["german"] + "   =>  " + word["english"])
        print("Want to keep practicing words you don't know? (Y/N)")
        keep_practicing = input()
        if keep_practicing == "Y":
            practice_nouns(pracetice_words)
        else:
            print("ok! schüss..")
   
practice_nouns()