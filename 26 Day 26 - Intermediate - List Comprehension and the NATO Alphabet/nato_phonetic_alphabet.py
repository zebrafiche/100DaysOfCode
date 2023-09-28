import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
# data_df = pandas.DataFrame(data)

new_phonetic_dict = {rows.letter: rows.code for (index, rows) in data.iterrows()}

user_input = input('Enter your word: ').upper()
output = [new_phonetic_dict[i] for i in user_input]
print(output)
