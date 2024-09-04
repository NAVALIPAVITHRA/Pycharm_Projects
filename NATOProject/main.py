import pandas as pd
data =pd.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

#TODO 1. Create a dictionary in this format:
phonetic = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input = input("enter a word: ").upper()
output = [phonetic[letter] for letter in input]
print(output)


