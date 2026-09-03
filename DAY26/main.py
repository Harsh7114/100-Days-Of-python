student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
### METHOD 1 ANGELA
dictionary={row.letter:row.code for (index, row) in data.iterrows()}
##### METOD 2 MINE

#print(data["letter"])
data_dict={}
for i in range(0,26):
        data_dict.update({data["letter"][i]: data["code"][i]})

print(data_dict)

def generate_phonetic ():
    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    user_word = input("Enter a word :").upper()
    try:

        ###METHOD 1 ANGELA
        output_list = [dictionary[letter] for letter in user_word]
        print(output_list)
        ### METHOD 2  MINE
        list =[]
        for i in user_word:
            list.append(data_dict[i])
        print(list)
    except KeyError:
        print("Enter the word between a-z and A-Z only")
        generate_phonetic()
generate_phonetic()

