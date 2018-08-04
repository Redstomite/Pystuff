x = 0
new_list = []
error = ""
finished_stage_one = "No"
word = list("Rahul")
sequence_list = ["R", "a", "h", "c", "l", "u", "g", "m"]
for value in word:
	if value not in sequence_list:
		error = "Y"

if error == "Y":
	print("Error, word cannot be made")
else:
	for value in sequence_list:
		if value in word:
			new_list.append(value)
	for value in word:
		newvalue = new_list[x]
		x = x+1
		if value != newvalue:
			print("Not in order!")
			break
	else:
		print("All clear!")

