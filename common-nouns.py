import pandas as pd
import random
import time

nouns_df = pd.read_excel("./data/most-used-german-words.xlsx", sheet_name='nouns')
noun_data = nouns_df.set_index('german')['english'].to_dict()

def practice_nouns():
    print("How many words would you like to practice?")
    num_words = input()
    pracetice_words = []
    # random key and value
    for i in range(int(num_words)):
        random_word = random.choice(list(noun_data.items()))
        ger = random_word[0]
        eng = random_word[1]
        print(ger + ': ')
        answer = input()
        if answer == eng:
            print('CORRECT!')
        else:
            print('That is not correct, the correct answer is ' + eng)
            pracetice_words.append(ger)
    print("\n..............")
    print("These are words you should learn more: ")
    for word in pracetice_words:
        print(word + " ... means => " + noun_data[word])
    print("\n..............")

    print("Want to keep practicing words you don't know? (Y/N)")
    keep_practicing = input()
    if keep_practicing == "Y":
        practice_nouns()
    else:
        print("ok! schüss..")
   
practice_nouns()