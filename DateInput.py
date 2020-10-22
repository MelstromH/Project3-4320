import datetime
def DateInput():
    while True:
        #Collect dates from user and split into three different fields
        try:
            begin_date = input('Enter a beginning date in YYYY-MM-DD format: ')
            begin_year, begin_month, begin_day = map(int, begin_date.split('-'))
            date1 = datetime.date(begin_year, begin_month, begin_day)
            

            end_date = input('Enter a end date in YYYY-MM-DD format: ')
            end_year, end_month, end_day = map(int, end_date.split('-'))
            date2 = datetime.date(end_year, end_month, end_day)

            #Compare the dates to make sure they are valid
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
            
        #Using Try/Except to easily restart if an error occurs 
        except:
            print("Enter valid dates!")
            continue

    #Prints out the dates to make sure everything worked the way it's supposed to    
    print("Start date: " + str(date1))
    print("End date: " + str(date2))