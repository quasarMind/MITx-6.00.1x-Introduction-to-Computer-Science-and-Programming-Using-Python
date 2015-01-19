

substring = ""
currentOrder = 0

for letter in s:	
	if ord(letter) >= currentOrder:
		substring += letter
	else:
		substring += " " + letter
	#print substring

	currentOrder = ord(letter)
print max(substring.split(), key=len)