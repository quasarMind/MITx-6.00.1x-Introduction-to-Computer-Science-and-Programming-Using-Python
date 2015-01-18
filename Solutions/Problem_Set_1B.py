numBOB = 0
x = 0
for letter in s:
	x += 1
	if letter is 'b':
		sp = s.index('b')
		s = s[sp+1:]
		print (x * '#' + s)
		if len(s) >= 2 :
			if s[0] is 'o' and s[1] is 'b':
				numBOB += 1
				s = s[1:]
print numBOB