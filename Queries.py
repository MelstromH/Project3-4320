#Function one to get input for the stock symbol. 
userInput1 = input("Enter the stock symbol you are looking for:")

print("Your Choices are: Bar and Chart")

#Function two to get input on what chart they want.
userInput2 = input("Enter the type of chart you want:")

#If Else Loop for the Input
if (userInput2 == "Bar"):
    print("cool")
    

elif (userInput2 == "Line"):
    print("Very cool")
    

else:
    print("That is not a valid input your choices are Bar or Line. Please try again.")
    

print("Time Series Selections: 1.Intraday 2.Daily 3.Weekly 4.Monthly")


#Function Three to get input for the Time Series selection.
userInput3 = input("Enter the time series option you'd like:") 
