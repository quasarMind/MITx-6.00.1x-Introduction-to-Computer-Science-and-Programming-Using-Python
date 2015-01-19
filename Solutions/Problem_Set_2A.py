balance = 4500
annualInterestRate = 0.18
monthlyPaymentRate = 0.3

totalPaid = 0

for i in range(1,13):

	mini = monthlyPaymentRate*balance
	balance -= mini
	balance = balance * ( 1 + (annualInterestRate/12))

	totalPaid += mini

	print ("Month: " + str(i))
	print ("Minimum monthly payment: " + str(round(mini,2)))
	print ("Remaining balance: " + str(round(balance,2)))


print ("Total Paid: " + str(round(totalPaid,2)))
print ("Remaining balance: " + str(round(balance,2)))
