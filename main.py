from GraphFunc import *
from Queries import *
import requests
import json

userChoices = queries()

if(userChoices[2] == 1):
    payload = {'function':'TIME_SERIES_INTRADAY','symbol':userChoices[0],'interval':'30min','apikey':'P8HT9FLVF2HF2HZB'}
elif(userChoices[2] == 2):
    payload = {'function':'TIME_SERIES_DAILY','symbol':userChoices[0],'apikey':'P8HT9FLVF2HF2HZB'}
elif(userChoices[2] == 3):
    payload = {'function':'TIME_SERIES_WEEKLY','symbol':userChoices[0],'apikey':'P8HT9FLVF2HF2HZB'}
else:
    payload = {'function':'TIME_SERIES_MONTHLY','symbol':userChoices[0],'apikey':'P8HT9FLVF2HF2HZB'}

results = requests.get('https://www.alphavantage.co/query', params=payload)

print(results.text)

while True:
    # Collect dates from user and split into three different fields
    try:
        begin_date = input('Enter a beginning date in YYYY-MM-DD format: ')
        begin_year, begin_month, begin_day = map(int, begin_date.split('-'))
        date1 = datetime.date(begin_year, begin_month, begin_day)

        end_date = input('Enter a end date in YYYY-MM-DD format: ')
        end_year, end_month, end_day = map(int, end_date.split('-'))
        date2 = datetime.date(end_year, end_month, end_day)

        # Compare the dates to make sure they are valid
        if (begin_year > end_year):
            print("Enter valid dates")
            continue
        elif (begin_year == end_year):
            if (begin_month > end_month):
                print("Enter valid dates")
                continue
            elif (end_month > begin_month):
                break
            elif (end_month == begin_month):
                if (begin_day >= end_day):
                    print("Enter valid dates")
                    continue
                else:
                    break
        else:
            break

    # Using Try/Except to easily restart if an error occurs
    except:
        print("Enter valid dates!")
        continue

# Prints out the dates to make sure everything worked the way it's supposed to
print("Start date: " + str(date1))
print("End date: " + str(date2))


if userChoices[1] == 1:
    printBarGraph(userChoices[0], date1, date2, 1, userChoices[2])
else:
    printLineGraph(userChoices[0], date1, date2, 1, userChoices[2])

