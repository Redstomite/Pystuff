dictionary = {"1":"e" , "2":"a" , "3":"d" , "4":"c"}
Values_in_dictionary = dictionary.values()
word = "abcx"
word_list = list(word)
for value in word_list:
	if value not in Values_in_dictionary:
		print("Word letter not in dictionary")
		break
else:
		print("Word letters are in dictionary")
