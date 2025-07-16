'''
The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability that 
two people will have the same birthday even in a small group of people. In a group of 70 people, 
there’s a 99.9 percent chance of two people having a matching birthday. But even in a group as 
small as 23 people, there’s a 50 percent chance of a matching birthday. This program performs several
probability experiments to determine the percentages for groups of different sizes. We call these 
types of experiments, in which we conduct multiple random trials to understand the likely outcomes, 
Monte Carlo experiments.

You can find out more about the Birthday Paradox at https://en.wikipedia.org/wiki/Birthday_problem.

'''
import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of random date objects for birthdays."""
    birthdays = []
    for _ in range(numberOfBirthdays):
        # The year is irrelevant, so we use 2000.
        startOfYear = datetime.date(2000, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        # Append the birthday to the list.
        # Note that we don't need to check for duplicates here,
        # because we are only interested in the probability of at least one match.
        # If we wanted to check for duplicates, we would need to use a set or check
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the list."""
    # Convert the list of birthdays to a set to remove duplicates.
    uniqueBirthdays = set(birthdays)
    if len(uniqueBirthdays) < len(birthdays):
        # If there are duplicates, find one.
        for birthday in uniqueBirthdays:
            if birthdays.count(birthday) > 1:
                return birthday
    return None  # No matches found.

def main():
    print('Birthday Paradox, a Monte Carlo experiment.')
    print()
    print ('''The Birthday Paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.
    (It's not actually a paradox, it's just a surprising result.)
    ''')

    #Set up a tuple of the month names in order
    monthNames = ('January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December')
    
    while True: #Keep asking until the user enters a valid number of birthdays.
        print('How many birthdays shall I generate? (Max 100)')
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            numberOfBirthdays = int(response)
            break # User entered a valid number.

    #Generate and display the birthdays.
    print('Generating', numberOfBirthdays, 'birthdays...')
    birthdays = getBirthdays(numberOfBirthdays)
    for i, birthday in enumerate(birthdays):
        monthName = monthNames[birthday.month - 1] # Get the month name from the tuple.
        ordinal = 'th' if (4 <= birthday.day <= 20) else {1: 'st', 2: 'nd', 3: 'rd'}.get(birthday.day % 10, 'th')
        print('Birthday #{}: {} {}{}'.format(i + 1, monthName, birthday.day, ordinal))

    print()  # Print a newline for better readability.
    input('> Press Enter to continue...')
    # Check for matches.
    print('Checking for matching birthdays...') 
    match = getMatch(birthdays)
    if match != None:
        monthName = monthNames[match.month - 1]
        ordinal = 'th' if (4 <= match.day <= 20) else {1: 'st', 2: 'nd', 3: 'rd'}.get(match.day % 10, 'th')
        print('Matching birthday found:', monthName, match.day, ordinal)
    else:
        print('No matching birthdays found.')
    print('Done.')
    print()


    # Run through 100,000 simulations:
    print('Generating', response, 'random birthdays 100,000 times...')
    numberOfBirthdays = int(response)
    print('This may take a while...')
    input('Press Enter to begin...')
    print('Let\'s run another 100,000 simulations.')
    simMatch = 0  # How many simulations had matching birthdays in them.
    for i in range(100_000):
        # Report on the progress every 10,000 simulations:
        if i % 10_000 == 0:
            print(i, 'simulations run...')
        birthdays = getBirthdays(numberOfBirthdays)
        if getMatch(birthdays) != None:
            simMatch = simMatch + 1
    print('100,000 simulations run.')

    # Display the results:
    print('Out of 100,000 simulations of', numberOfBirthdays, 'birthdays, there were',
          simMatch, 'simulations with matching birthdays.')
    probability = round(simMatch / 100_000 * 100, 2)
    print('This means that the probability of two people having matching birthdays in a group of', response,
          'is about', probability, '%.')
    print('This is surprisingly high, even for a group as small as', response, '.')
    print('Thanks for playing!')

if __name__ == '__main__':
    main()

