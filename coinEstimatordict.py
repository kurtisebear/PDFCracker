
# -*- coding: utf-8 -*-

weights = {
	'one pence':  3.56,
	'two pence' : 7.13,
	'five pence' : 3.25,
	'ten pence' : 6.50,
	'twenty pence' : 5.00,
	'fifty pence' : 8.00,
	'one pound' : 9.5

}



weightlist = (
	('one pence',3.56, 0.01),
	('two pence', 7.13, 0.02),
	('five pence', 3.25, 0.05),
	('ten pence', 6.50, 0.10),
	('twenty pence', 5.00, 0.20),
	('fifty pence', 8.00, 0.50),
	('one pound', 9.5, 1)
)


userweights ={}



for key, weight, value in weightlist:
	p = input("Please enter the weight of " + key + " coins you have in grams? ")
	amount = int(p/weight)
	totalvalue = (amount * value)
	printvalue = 'YOu have: {0} coins, they are worth:£{1}'.format(amount, totalvalue)
	print printvalue




#for key, weight in weights.iteritems():
#	p = input("Please enter the weight of " + key + " coins you have in grams? ")
#	amount = int(p / value)
	
	