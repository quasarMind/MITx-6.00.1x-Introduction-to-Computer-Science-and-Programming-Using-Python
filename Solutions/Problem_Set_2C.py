remaining = balance

monthlyInterest = annualInterestRate/12
monthlyPaymentLow = balance /12
monthlyPaymentHigh = (balance * (1 + monthlyInterest)**12) / 12.0

monthlyPaymentRate = (monthlyPaymentLow + monthlyPaymentHigh )/2

while (True):
	
	remaining = balance

	for i in range(1,13):
		remaining = (remaining - monthlyPaymentRate )*(1+(annualInterestRate/12))

	#print ("Remaining in Loop: ") + str(remaining)
	
	if remaining > 0:
		monthlyPaymentLow = monthlyPaymentRate
		monthlyPaymentRate = (monthlyPaymentRate + monthlyPaymentHigh)/2
		
	elif remaining < 0:
		monthlyPaymentHigh = monthlyPaymentRate
		monthlyPaymentRate = (monthlyPaymentRate + monthlyPaymentLow)/2
		

	if abs(remaining - 0.0 ) < 0.0001:
		break

	#print "monthlyPaymentRate: " + str(monthlyPaymentRate)
	#print "#########"


#print "DONE"
print "Lowest Payment: " + str(round(monthlyPaymentRate,2))