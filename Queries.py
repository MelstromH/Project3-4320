userChoicelist = []

print("Stock Data Visualizer\n-----------------------\n")

# Function one to get input for the stock symbol.
userInput1 = input("Enter the stock symbol you are looking for: ")
userChoicelist.append(userInput1)

print("\nChart Types\n---------------")

print("1.Bar \n2.Chart\n")

# Function two to get input on what chart they want.
userInput2 = int(input("Enter the type of chart you want (1, 2): "))

while(True):
    if (userInput2 == 1):
        userChoicelist.append(userInput2)
        break

    elif (userInput2 == 2):
        userChoicelist.append(userInput2)
        break

    else:
        print("\nThat is not a valid input your choices are 1.Bar or Line. Please try again.\n")
        userInput2 = int(input("Enter the type of chart you want:"))

print("\nSelect the Time Series of the chart you want to Generate")
print("---------------------------------------------------------")
print("1.Intraday\n2.Daily\n3.Weekly\n4.Monthly\n")

# Function Three to get input for the Time Series selection.
userInput3 = int(input("Enter the time series option (1, 2, 3, 4): "))

while(True):
    if (userInput3 > 0 & userInput3 < 5):
        userChoicelist.append(userInput3)
        break

    else:
        print("\nThat is not a valid input your choices are \n1.Intraday \n2.Daily \n3.Weekly \n4.Monthly\n")
        userInput3 = int(input("Enter the time series option you'd like:"))
