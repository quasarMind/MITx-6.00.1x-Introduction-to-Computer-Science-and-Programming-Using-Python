monthlyPaymentRate = -10.0
remaining = balance

while (remaining > 0):

	remaining = balance
	monthlyPaymentRate += 10

	for i in range (1,13):
		remaining = ( remaining - monthlyPaymentRate )*(1+(annualInterestRate/12))

	
	
	# print "Remaining: " + str(remaining)
	# print "monthlyPaymentRate: " + str(monthlyPaymentRate)
	# print  "#############################################"

#print ("DONE CALCULATING")
#print "Remaining: " + str(remaining)
print "Lowest Payment: " + str(monthlyPaymentRate)