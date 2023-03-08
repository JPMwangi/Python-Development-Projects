student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import code
import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# loop through a data frame
# for (key, value) in student_data_frame.items():
#     pass

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row.score)
    #Access index and row
    #Access row.student or row.score
    pass
    
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
data = pandas.read_csv("One Bite At A Time/Day 26/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
# TODO loop through the csv file
for (index, row) in data.iterrows():
    nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(nato_dict)
    
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

output_list = [nato_dict[letter] for letter in word]

print(output_list)
