import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'C:/Users/Softpro/Downloads/chicago.csv',
              'new york city': 'C:/Users/Softpro/Downloads/new_york_city.csv',
              'washington': 'C:/Users/Softpro/Downloads/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    city =""
    #create a list of availabel cities:
    cities_list = ["chicago","new york city","washington"]
    
    while city not in cities_list:
        city = input ("Which city would you like to see data for from the following cities: (chicago, new york city, washington)?\n").lower()
    
    # get user input for month (all, january, february, ... , june)
    month = ""
    #create a list of available months including "all" option:
    months_list = ["january","february","march","april","may","june","all"]
    
    while month not in months_list:
        month = input ("Which month would you like to see data for from the following months: (january, february, march, april, may, june or all)?\n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    #create a list of days of the week available including "all" option:
    days_list = ["monday", "tuesday", "widnesday", "thrusday", "friday", "saturday", "sunday" , "all"]
    
    while day not in days_list:    
        day = input ("Which day of week would you like to see data for from the following days: (monday, tuesday, widnesday, thrusday, friday, saturday, sunday or all?)\n").lower()
    print ("\nYou have chosen the following:")
    print ("The City: ", city)
    print ("Month: ", month)
    print ("Day: " , day)
    print('-'*70)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
   
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month_name()
    popular_month = df["month"].mode()[0]
    print ("The most common month is ", popular_month)
    
    # display the most common day of week
    popular_day = df["day_of_week"].mode()[0]
    print ("The most common day of week is ", popular_day)
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df["Start Time"].dt.hour
    # display the most common start hour
    popular_hour = df["hour"].mode()[0]
    print ("The most common hour is ", popular_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print ("The most commonly used start station is ", popular_start_station)
    
    # display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print ("The most commonly used end station is ", popular_end_station)
    
    # display most frequent combination of start station and end station trip
    # create new column "Start to End" by combining the two colunms "Start Station" and "End Station"
    df["Start to End"] = df["Start Station"] +" to "+ df["End Station"]
    popular_trip = df["Start to End"].mode()[0]
    print ("\nThe most frequent combination of start station and end station is " , popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    # total trip time in seconds:
    total_time = df["Trip Duration"].sum()
    # display total travel time in days, hours, minutes, seconds:
    if total_time < 60:
        print ("The total trip time is {} seconds.".format(total_time))
    elif total_time >= 60 and total_time < 3600:
        seconds = total_time % 60
        minutes = total_time // 60
        print ("The total trip time is {} minutes and {} seconds.".format(minutes, seconds) )
    elif total_time >= 3600 and total_time < 24*3600:
        hours = total_time // 3600
        total_time %= 3600
        minutes = total_time // 60
        total_time %= 60
        seconds = total_time
        print ("The total trip time is {} hours, {} minutes and {} seconds.".format(hours,minutes,seconds))
    else:
        days = total_time // (24 * 3600)
        total_time = total_time % (24 * 3600)
        hours = total_time // 3600
        total_time %= 3600
        minutes = total_time // 60
        total_time %= 60
        seconds = total_time
        print ("The total trip time is {} days, {} hours, {} minutes and {} seconds.".format(days,hours,minutes,seconds))
    
    # mean travel time in seconds:
    mean_time = df["Trip Duration"].mean()
    # dispay mean travel time in days, hours, minutes, seconds:
    if mean_time < 60:
        print ("The mean trip time is {} seconds.".format(mean_time))
    elif mean_time >= 60 and mean_time < 3600:
        seconds = mean_time % 60
        minutes = mean_time // 60
        print ("The mean trip time is {} minutes and {} seconds.".format(minutes, seconds) )
    elif mean_time >= 3600 and mean_time < 24*3600:
        hours = mean_time // 3600
        mean_time %= 3600
        minutes = mean_time // 60
        mean_time %= 60
        seconds = mean_time
        print ("The mean trip time is {} hours, {} minutes and {} seconds.".format(hours,minutes,seconds))
    else:
        days = mean_time // (24 * 3600)
        mean_time = mean_time % (24 * 3600)
        hours = mean_time // 3600
        mean_time %= 3600
        minutes = mean_time // 60
        mean_time %= 60
        seconds = mean_time
        print ("The mean trip time is {} days, {} hours, {} minutes and {} seconds.".format(days,hours,minutes,seconds))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)



def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df["User Type"].value_counts()
    print ("The types of users in numbers:\n" , user_type)
    
    # Display counts of gender
    if city in ["chicago" , "new york city"]: # there is no "Gender" column in washington
        gender = df["Gender"].value_counts()
        print ("\nThe gender of users in numbers:\n" , gender)
        
        # Display the earliest year of birth:
        earliest = int(df["Birth Year"].min())
        print ("\nThe earliest year of birth is ", earliest)
        # Display the most recent year of birth:
        recent = int(df["Birth Year"].max())
        print ("The most recent year of birth is ", recent)
        # Display the most common year of birth:
        common =int(df["Birth Year"].mode()[0])
        print ("The most common year of birth is ", common)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def data_sample(df):
    """
   Display samples of 5 rows on demand .
   Args:
       df - The Whole Pandas DataFrame
   Returns:
       df - Sample of 5 Rows from the whole Pandas DataFrame
   """
    demand = input('Would you like to see sample of raw data? Yes/No\n').lower()

    if demand == 'yes':
	pd.set_option('display.max_columns',200)
        print(df.sample(5))
        return data_sample(df)
    elif demand == 'no':
        return None
    else:
        print('Unknown Entry!')
        return data_sample(df)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        data_sample(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
