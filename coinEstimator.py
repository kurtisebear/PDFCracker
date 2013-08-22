
#varibles for the weight of coins

onep = 3.56
twop = 7.13
fivep = 3.25
tenp = 6.50
twentyp = 5.00
fiftyp = 8.00
onepound = 9.5



# ask for input

amountone = input("Please enter the weight of your 1p\'s in grams?  ")
amounttwo = input("Please enter the weight of your 2p\'s in grams?  ")
amountfive = input("Please enter the weight of your 5p\'s in grams?  ")
amountten = input("Please enter the weight of your 10p\'s in grams?  ")
amounttwenty = input("Please enter the weight of your 20p\'s in grams?  ")
amountfifty = input("Please enter the weight of your 50p\'s in grams?  ")
amountonepound = input("Please enter the weight of your 1 pound's in grams?  ")





# return estimate of coin worth



#return estimate of total amount of coins
#amount of coins will be varibles / total weight

print "-" * 10
print "Total Amount Of Coins"

print1 = "you have " + str(round(amountone/onep)) + " one pence coins"
print2 = "you have " + str(round(amounttwo/twop)) + " two pence coins"
print3 = "you have " + str(round(amountfive/fivep)) + " five pence coins"
print4 = "you have " + str(round(amountten/tenp)) + " ten pence coins"
print5 = "you have " + str(round(amounttwenty/twentyp)) + " twenty pence coins"
print6 = "you have " + str(round(amountfifty/fiftyp)) + " fifty pence coins"
print7 = "you have " + str(round(amountonepound/onepound)) + " one pound coins"





print print1
print print2
print print3
print print4
print print5
print print6
print print7


