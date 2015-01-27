def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)





def radiationExposure(start, stop, step):

	#My Code Is Below
	radiationAmount = 0
	x = start
	while (x< stop): # x isnt <= stop, becasue when x=stop,
	# the calculated value will be an overshoot
		radiationAmount +=  step*f(x)
		x += step 
	print radiationAmount	
	# return radiationAmount



radiationExposure(5,11,1)
