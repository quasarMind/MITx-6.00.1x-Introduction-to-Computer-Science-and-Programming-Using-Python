vowels = ['a','e','i','o','u']
numVowels = 0

for letter in s:
	if letter in vowels:
		numVowels += 1
print (numVowels)