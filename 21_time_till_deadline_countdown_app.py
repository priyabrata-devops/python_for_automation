import datetime

user_input = input("enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

print(input_list)

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

#print(type(deadline_date))

todate_time = datetime.datetime.today()

time_till = deadline_date - todate_time

hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"Dear user! time remaining for your goal: {goal} is {hours_till} hours.")