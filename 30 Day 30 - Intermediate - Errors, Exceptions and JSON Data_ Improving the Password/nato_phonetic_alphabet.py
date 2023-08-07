import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
# data_df = pandas.DataFrame(data)

new_phonetic_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}


def generate_phonetic():
    user_input = input('Enter your word: ').upper()
    try:
        output = [new_phonetic_dict[i] for i in user_input]
    except KeyError:
        print('Only letters in the alphabet please')
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
