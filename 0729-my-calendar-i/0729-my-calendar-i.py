class MyCalendar:

    def __init__(self):
        self.booked_dates = []

    def book(self, startTime: int, endTime: int) -> bool:
        for date in self.booked_dates:
            if date[0] < endTime and date[1] > startTime:
                return False
        self.booked_dates.append((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)