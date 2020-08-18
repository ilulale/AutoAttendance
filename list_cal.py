import datetime
from cal_setup import get_calendar_service

def geturlcal():
   service = get_calendar_service()
   # Call the Calendar API
   now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
   events_result = service.events().list(
       calendarId='primary', timeMin=now,
       maxResults=1, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])

   if not events:
       return 0
   for event in events:
       start = event['start'].get('dateTime', event['start'].get('date'))
    #    print(start, event['summary'])
       return event['description']


def getnamecal():
   service = get_calendar_service()
   # Call the Calendar API
   now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
   events_result = service.events().list(
       calendarId='primary', timeMin=now,
       maxResults=1, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])

   if not events:
       return 0
   for event in events:
       start = event['start'].get('dateTime', event['start'].get('date'))
    #    print(start, event['summary'])
       return event['summary']

