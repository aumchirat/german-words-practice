import pandas as pd
import random

nouns_df = pd.read_excel("./data/most-used-german-words.xlsx", sheet_name='nouns')
noun_data = nouns_df.set_index('german')['english'].to_dict()
# for key, value in noun_data.items():
#     print(key, ':', value)

# let user choose how many words they'd like to practice
num_words = 2
pracetice_words = []
# random key and value
for i in range(num_words):
    random_word = random.choice(list(noun_data.items()))
    ger = random_word[0]
    eng = random_word[1]
    print(ger + ': ')
    answer = input()
    if answer == eng:
        print('CORRECT!')
    else:
        print('That is not correct, save this word for later? (Y/N)')
        save_word = input()
        if save_word == 'Y':
            pracetice_words.append(ger)


print(pracetice_words)