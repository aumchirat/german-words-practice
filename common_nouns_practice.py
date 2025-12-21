import pandas as pd
import random
import sys

nouns_df = pd.read_excel("./data/most-used-german-words.xlsx", sheet_name='nouns')
# noun_data = nouns_df.set_2index('german')['english'].to_dict()
noun_data = nouns_df.to_dict('records')

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
            # update by delete the word from updated_pracetice set
            print('CORRECT!')
            del practice_set[random_num]
        else:
            print('That is not correct, the correct answer is ' + practice_set[random_num]["english"])
            pracetice_words.append(practice_set[random_num])
    # if there're still words to learn
    if len(pracetice_words) > 0:
        print("...words that you should practice more....: ")
        for word in pracetice_words:
            print(word["german"] + " => " + word["english"])

print("Schüss..")
   
practice_nouns()