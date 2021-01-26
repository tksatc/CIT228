import datetime
# weekdays tuple
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# retrieving current date
now = datetime.date.today()
# retrieve the day of the week which is an integer
dayOfWeek = now.weekday()
# subscript into weekDays using the dayOfWeek
today = weekDays[dayOfWeek]
# calculate and print days until the weekend
daysToWeekend = 6 - dayOfWeek
print("There are ", daysToWeekend-1, " days until the weekend")
# flag to only print 1 quote in for loop
quotePrinted = "false"
# prints week days left until weekend with a quote
for left in weekDays[dayOfWeek:daysToWeekend]:
    if today == "Sunday" and quotePrinted == "false":
        print(left, " it's still the weekend!")
        quotePrinted = "true"
    elif (today == "Monday" or today == "Tuesday" or today == "Wednesday") and quotePrinted == "false":
        print(left, " too many days remaining")
        quotePrinted = "true"
    elif today == "Thursday" and quotePrinted == "false":
        print(left, " get ready!")
        quotePrinted = "true"
    elif quotePrinted == "false":
        print(left, " we made it!")
        quotePrinted = "true"
    else:
        print(left)