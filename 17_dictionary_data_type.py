def days_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} {conversion_unit}"
    else:
        return "Unsupported Unit"

def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])

        if user_input_number > 0:
            days_of_unit = days_to_unit(user_input_number, days_and_unit_dictionary["unit"])
            print(days_of_unit)
        elif user_input_number == 0:
            print("You entered 0 value, Please enter a valid positive number")
        else:
            print("You entered negative value, Please enter a valid positive number")
    
    except ValueError:
        print("Your input is not a number, Don't ruin my program")

user_input = ""
while user_input != "exit":
    user_input = input("Hey USER, enter number of days & conversion unit!\n") # input() always returns a string
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()



'''my_dictionary = {"days": "10", "unit": "hours"}
print(my_dictionary["unit"])'''