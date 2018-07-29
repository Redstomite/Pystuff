dictionary = {"1":"e" , "2":"a" , "3":"d" , "4":"c"}
allvalues = dictionary.values()
word = "abcx"
lword = list(word)
for value in lword:
	if value not in allvalues:
		print("Word letter not in dictionary")
		break
else:
	print("Word letters are in dictionary")
