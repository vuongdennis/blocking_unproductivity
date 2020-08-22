import datetime as dt

class Time:
    def __init__(self, hour, minute):
        self.minute = int(minute)
        self.hour = int(hour)

    def get_hour(self):
        if dt.datetime.now().hour > 12:
            return dt.datetime.now().hour - 12
        else:
            return dt.datetime.now().hour
    
    def get_minutes(self):
        return dt.datetime.now().minute

    def check(self):
        if (self.hour == self.get_hour()) and (self.minute == self.get_minutes()):
            return True
        else:
            return False