# question about current age
age = int(input("What is your age currently?"))

# years left
years_remaining = 90-age

# days left
daysLeft = years_remaining * 365

# weeks left
weeksLeft = years_remaining * 52

# months left
monthsLeft = years_remaining * 12

# message var
message = "You have {daysLeft} days, {weeksLeft} weeks, or {monthsLeft} months left to live."

# print the message
print(message)


