import calendar


class Calendar:
    def __init__(self, month, year):
        self.month = month
        self.year = year

    def display(self):
        cal = calendar.monthcalendar(self.year, self.month)
        print(calendar.month_name[self.month] + " " + str(self.year))
        print("MO TU WE TH FR SA SU")
        for week in cal:
            week_str = ""
            for day in week:
                if day == 0:
                    week_str += "   "
                else:
                    week_str += "{:2d} ".format(day)
            print(week_str)

    def events(self, day, event):
        cal = calendar.Calendar()
        for d in cal.itermonthdates(self.year, self.month):
            if d.month == self.month and d.day == day:
                print("Added Event '{}' on {}".format(event, d.strftime("%Y-%m-%d")))
                break


if __name__ == "__main__":
    cal = Calendar(12, 2023)
    cal.display()
    cal.events(11, "Friends BirthDay")
