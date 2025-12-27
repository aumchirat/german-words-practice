import pandas as pd
import random

nouns_df = pd.read_excel("./data/most-used-german-words.xlsx", sheet_name='nouns')
noun_data = nouns_df.to_dict('records')
noun_dict = {}
# {'das Land': 'land|country|state', 'das Jahr': 'year',...}
for word_dict in noun_data:
    noun_dict[word_dict['german']] = word_dict['english']

def get_random_word():
    words = nouns_df.iloc[:, 0].to_list()
    random_word = random.choice(words)
    return random_word

def check_answer(word, user_answer):
    correct_answers = noun_dict[word]
    correct_answers = correct_answers.split("|")
    if user_answer in correct_answers:
        return "correct!"
    else:
        return f"that's not correct, the answer is {", ".join(correct_answers)}"

