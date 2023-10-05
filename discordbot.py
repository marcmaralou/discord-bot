import requests
import datetime
import schedule
import time


def rolling():
    response = requests.post('{REQUEST URL}',
                             data = {'content':'$p'},
                             headers = {'authorization':'{AUTHORIZATION TOKEN}'})
    # for post url: send message to channel > right click web browser chatbox > inspect > network > messages > headers > general > request url
    # for auth token: send message to channel > right click web browser chatbox > inspect > network > messages > headers > request headers > authorization
    if response.status_code == 200:
        print(f'rolled @ {datetime.datetime.now().strftime("%-I:%M:%S%p").replace("AM","am").replace("PM","pm")},',
              f'next roll @ {(datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%-I:00%p").replace("AM","am").replace("PM","pm")}')
    elif response.status_code == 401:
        print(f'error {response.status_code}: update authorization token')
    else:
        print(response.status_code)

def firstRollTime():
    if int(datetime.datetime.now().strftime('%H')) % 2 == 1:
        return (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%-I:00%p").replace('AM','am').replace('PM','pm')
    else:
        return (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%-I:00%p").replace('AM','am').replace('PM','pm')

print(f'rolling @ {firstRollTime()}')

schedule.every().day.at("01:00").do(rolling)
schedule.every().day.at("03:00").do(rolling)
schedule.every().day.at("05:00").do(rolling)
schedule.every().day.at("07:00").do(rolling)
schedule.every().day.at("09:00").do(rolling)
schedule.every().day.at("11:00").do(rolling)
schedule.every().day.at("13:00").do(rolling)
schedule.every().day.at("15:00").do(rolling)
schedule.every().day.at("17:00").do(rolling)
schedule.every().day.at("19:00").do(rolling)
schedule.every().day.at("21:00").do(rolling)
schedule.every().day.at("23:00").do(rolling)

while True: # necessary to keep program running per schedule docs
    schedule.run_pending()
    time.sleep(1)
