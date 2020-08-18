from datetime import datetime, timedelta
from cal_setup import get_calendar_service
from getdate import startweek
import calendar


def addevent(d,lec,time,link):
   # creates one hour event tomorrow 10 AM IST
   service = get_calendar_service()

   tst = datetime(d.year, d.month, d.day, time)
   start = tst.isoformat()
   end = (tst + timedelta(hours=2)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'MataAuto ' + lec,
           "description": link,
           "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
           "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

# a = startweek()
# addevent(a,'DBMS',11)

def chselect(ch):
    ch = int(ch)
    lec = ''
    link = ''
    if (ch == 1):
        lec = 'DBMS'
        link = 'https://meet.google.com/lookup/cg4pr4khrf'
    elif (ch == 2):
        lec = 'MP'
        link = 'https://meet.google.com/lookup/elp54h7dks'
    elif (ch == 3):
        lec = 'CN'
        link = 'nut'
    elif (ch == 4):
        lec = 'TCS'
        link = 'nut'
    elif (ch == 5):
        lec='Miniproject'
        link='nut'
    return lec,link

print('Lets make the timetable for the week \n')
din=0
rghnw = startweek()
while(din<5):
    print('----------------------------------------------------------------')
    print(calendar.day_name[rghnw.weekday()])
    ch = input('''First Lecutre:-
    1. DBMS 
    2. MP
    3. CN
    4. TCS
    5. MiniProject
    ''')
    lec,link = chselect(ch)
    addevent(rghnw,lec,11,link)
    ch = input('''Second Lecutre:-
    1. DBMS 
    2. MP
    3. CN
    4. TCS
    5. MiniProject
    ''')
    lec,link = chselect(ch)
    addevent(rghnw,lec,14,link)
    din = din+1
    rghnw = rghnw + timedelta(days=1)