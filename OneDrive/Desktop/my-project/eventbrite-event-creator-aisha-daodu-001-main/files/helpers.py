
import webbrowser
import datetime
import os

# These functions are provided for you, you don't need to change any of the code here.

def get_api_key():
    '''Read the api key from the apikey.txt file'''
    apikey_path = os.path.join(os.getcwd(), "files", "apikey.txt")
    if not os.path.exists(apikey_path):
        raise Exception("Please create a file named apikey.txt in the files folder and paste the Private Token there")
    
    with open(apikey_path) as f:
        return f.read().strip()

    
def open_url_in_browser(url):
    '''Opens a url on your computer'''
    webbrowser.open(url, new=1, autoraise=True)

def get_formatted_day_and_time(duration_hours=1):
    '''Asks user for a day and time, then formats it in a way that the eventbrite api expects.
    If user provides invalid input, try again.'''
    
    while True:
        days_in_future = input('The event starts how many days in the future? ')
        hour = input('Please enter the hour of the day, for example 10 ')
        try:
            days_in_future = int(days_in_future)
            hour = int(hour)
        except ValueError:
            print('Could not parse, please enter a number')
            continue
        
        start_time_utc = get_formatted_day_and_time_utc(days_in_future, hour, 0)
        end_time_utc = get_formatted_day_and_time_utc(days_in_future, hour, duration_hours)
        return start_time_utc, end_time_utc
        

def get_formatted_day_and_time_utc(days_in_future, hour, add_hours):
    '''Formats a day+time in a way that the eventbrite api expects,
    including converting to UTC timezone'''
    
    today = datetime.datetime.today()
    date = today + datetime.timedelta(days=int(days_in_future))
    date_with_time = date.replace(hour=int(hour), minute=0, second=0)
    
    # convert from current timezone to utc
    dt_utc = date_with_time.astimezone(datetime.timezone.utc)
    dt_utc += datetime.timedelta(hours=add_hours)
    result = dt_utc.isoformat(sep='T', timespec='seconds')
    return result.split('+')[0] + 'Z'

