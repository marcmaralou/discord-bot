import requests # https://requests.readthedocs.io/en/latest/
import datetime # https://docs.python.org/3/library/datetime.html
import schedule # # https://schedule.readthedocs.io/en/stable/
import time # https://docs.python.org/3/library/time.html

# https://mudae.fandom.com/wiki/Pok%C3%A9slot why i made this

header = { # right click chat box > inspect > network > messages > headers > authorization
    'authorization': 'Mzc2NDI4NDk5MjAxOTQ5NzA5.Gdga7g.GnaV5Zwu3wNzkQYy9uqFKpwWsEYs6m3_KuBrUQ'
} # changes whenver you have account changes

payload = { # this is the message to send
    'content': '$p' # https://mudae.fandom.com/wiki/Pok%C3%A9slot#List_of_Commands
}

def escortThePayload(): # references: https://www.youtube.com/watch?v=DArlLAq56Mo and https://github.com/nonrice/discord-auto-message
    r = requests.post('https://discord.com/api/v9/channels/808945581518225438/messages', data=payload, headers=header)

    if r.status_code == 200: # success!
        print(f'$p sent @ {datetime.datetime.now().strftime("%H:%M:%S")}')
        print(f'sending next message @ {(datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%H:%M:00")}')
    
    elif r.status_code == 401: # need to update authorization token
        print(f'error {r.status_code}: unauthorized')
        
    else:
        print(r.status_code)

def first(): # determing time and adjusting accordingly to display right time for next iteration
    if int(datetime.datetime.now().strftime('%H')) % 2 == 0:
        return (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%H:00")
    
    else:
        return (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime("%H:00")

# def ellipsis(): # got from here https://stackoverflow.com/questions/58212749/triple-dots-animation-while-program-is-loading-in-terminal
#     print(end=f'sending next message @ {(datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%H:%M")}')

#     periods = 0
#     while int(datetime.datetime.now().strftime('%H')) % 2 != 0:
#         if periods == 3:
#             print(end='\b\b\b', flush=True)
#             print(end='   ',    flush=True)
#             print(end='\b\b\b', flush=True)
#             periods = 0

#         else:
#             print(end='.', flush=True)
#             periods += 1

#         time.sleep(1)

print(f'sending first message @ {first()}')
# ellipsis()

schedule.every().day.at("00:00").do(escortThePayload)
schedule.every().day.at("02:00").do(escortThePayload)
schedule.every().day.at("04:00").do(escortThePayload)
schedule.every().day.at("06:00").do(escortThePayload)
schedule.every().day.at("08:00").do(escortThePayload)
schedule.every().day.at("10:00").do(escortThePayload)
schedule.every().day.at("12:00").do(escortThePayload)
schedule.every().day.at("14:00").do(escortThePayload)
schedule.every().day.at("16:00").do(escortThePayload)
schedule.every().day.at("18:00").do(escortThePayload)
schedule.every().day.at("20:00").do(escortThePayload)
schedule.every().day.at("22:00").do(escortThePayload)

while True: # necessary to keep it running, per schedule docs
    schedule.run_pending()
    time.sleep(1)

# js bot? to maybe host it on netlify
# total messages sent using program?
# sending next message... then have it rewrite the line with sent @?