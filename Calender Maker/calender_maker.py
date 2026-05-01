"""
--------------------------------------
Calender Maker: Create Monthly Calender, saved to a text file and fit for printing out.

This program generates printable text files of monthly calendars for the month and year 
you enter. Dates and calendars are a tricky topic in programming because there are so 
many different rules for determining the number of days in a month, which years are 
leap years, and which day of the week a particular date falls on.

This program focuses on generating the multiline string for the monthly calendar page.
-------------------------------------
"""

#Importing important packages
import datetime

#Set up the constants:
DAYS = ('Sunday','Monday','Tuesday', 'Wednesday','Thursday','Friday','Saturday')
MONTHS = ('January','February','March','April','May','June','July','August','September','October','November','December')

#Define the get calender method

def getCalenderFor(year, month):
    calText = '' #calText will contain the string of our calender.

    #Put the month and year at the top of the calender:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    #  # Add the days of the week labels to the calendar:
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # The horizontal line string that separate weeks:
    weekSeparator = ('+----------' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blankRow = ('|          ' * 7) + '|\n'

    #Get the first date in the month. 
    currentDate= datetime.date(year, month, 1)

    #Roll back currentDate until it is Sunday. (weekday() returns 6 for Sunday, not 0)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days = 1)
    
    while True: #Loop over each week in the month
        calText += weekSeparator

        #dayNumberRow is the row with the day number labels:
        dayNumberRow = ''

        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Go to next day
        dayNumberRow += '|\n' # Add the vertical line after Saturday

        # Add the day number row and 3 blank rows to the calender text.
        calText +=dayNumberRow
        for i in range(3):
            calText+= blankRow
        
        #Check if we're done with the month:
        if currentDate.month != month:
            break

    #Add the horizontal line at the very bottom of the calender
    calText += weekSeparator
    return calText


# Writing the main function 

def main():

    try:

        print('Calender Maker, by Sam')

        #Loop over to collect year details from the user
        while True:
            print ('Enter the year for your calender: ')
            response = input('> ')

            if response.isdecimal() and int(response)>0:
                year = int(response)
                break

            else:
                print ('Please enter a numeric year, like 2026. ')
            
            continue

        #Loop to get a month from the user.
        while True:
            print ('Enter the month for the calender, 1-12: ')
            response = input('> ')

            if not response.isdecimal():
                print ('Please enter a numeric month, like 3 for March. ')
                continue

            month = int(response)
            if 1<= month <=12 :
                break

            print ('Please enter a number from 1 to 12. Like 12 for December. ')

        calText = getCalenderFor(year, month)
        print(calText) # Display the calender.

        # Save the Calender to a text file:
        calenderFilename = 'calender_{}_{}.txt'.format(year, month)
        with open(calenderFilename, 'w') as fileObj:
            fileObj.write(calText)

        print ('Saved to '+ calenderFilename)
        print ('Thanks for using the Calender App')

    except Exception as e :

        print ('The calender maker failed due to :', e)


if __name__ == '__main__':
    main()