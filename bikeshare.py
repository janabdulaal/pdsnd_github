Explore US Bikeshare Data.

This script allows the user to explore data related to bikeshare systems
for three major cities in the United States: Chicago, New York City, and Washington.
The user can filter the data by city, month, and day of the week.

The program computes descriptive statistics and displays the raw data on request.

Author: Jana Abdulaal
import time
import pandas as pd

import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no filter
        (str) day - name of the day to filter by, or "all" to apply no filter

    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter a valid city name.")

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Which month? January, February, March, April, May, June or 'all'? ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month.")

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Which day? Monday, Tuesday, ... Sunday or 'all'? ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day.")
def get_valid_input(prompt, valid_options):
    Repeatedly prompt the user until a valid input is received.

    Args:
        prompt (str): The message to display to the user
        valid_options (list): List of valid options (strings)

    Returns:
        str: A valid user input
    while True:
        response = input(prompt).lower()
        if response in valid_options:
            return response
        print(f"Invalid input. Please choose from: {valid_options}")

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    city = get_valid_input("Would you like to see data for Chicago, New York City, or Washington? ",
                           ['chicago', 'new york city', 'washington'])
    month = get_valid_input("Which month? January, February, March, April, May, June or 'all'? ",
                            ['january', 'february', 'march', 'april', 'may', 'june', 'all'])
    day = get_valid_input("Which day? Monday, Tuesday, ... Sunday or 'all'? ",
                          ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'])

    return city, month, day

def load_data(city, month, day):
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no filter
        (str) day - name of the day to filter by, or "all" to apply no filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()
    print('Most Common Month:', df['month'].mode()[0])
    print('Most Common Day of Week:', df['day_of_week'].mode()[0])
    print('Most Common Start Hour:', df['Start Time'].dt.hour.mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))

def common_start_station(df):
    print('Most Common Start Station:', df['Start Station'].mode()[0])

def common_end_station(df):
    print('Most Common End Station:', df['End Station'].mode()[0])

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()
    print('Most Common Start Station:', df['Start Station'].mode()[0])
    print('Most Common End Station:', df['End Station'].mode()[0])
    common_start_station(df)
    common_end_station(df)
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    print('Most Common Trip:', df['Trip'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...')
    start_time = time.time()
    print('Total Travel Time:', df['Trip Duration'].sum())
    print('Average Travel Time:', df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))

def user_stats(df):
    print('\nCalculating User Stats...')
    start_time = time.time()
    print('User Types:\n', df['User Type'].value_counts())
    if 'Gender' in df.columns:
        print('\nGender Counts:\n', df['Gender'].value_counts())
    if 'Birth Year' in df.columns:
        print('\nEarliest Birth Year:', int(df['Birth Year'].min()))
        print('Most Recent Birth Year:', int(df['Birth Year'].max()))
        print('Most Common Birth Year:', int(df['Birth Year'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))

def display_raw_data(df):
    """Displays raw data 5 rows at a time upon user request."""
    index = 0
    while True:
        show_data = input("\nWould you like to see 5 lines of raw data? Enter yes or no: ").lower()
        if show_data == 'yes':
            print(df.iloc[index:index+5])
            index += 5
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
