dictionary = {"1":"e" , "2":"a" , "3":"d" , "4":"c"}
Values_in_dictionary = dictionary.values()
word = "abcx"
word_list = list(word)
how_many_chars_not_in_word_list = 0
for value in word_list:
	if value not in Values_in_dictionary:
		how_many_chars_not_in_word_list = how_many_chars_not_in_word_list + 1

if how_many_chars_not_in_word_list == 0:
	print("Words can be made by the letters in the dictionary")
elif how_many_chars_not_in_word_list >= 0:
	print("Letter/s not in dictionary.", how_many_chars_not_in_word_list , "letters were not found in dictionary.")
