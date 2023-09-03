def days_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} {conversion_unit}"
    else:
        return "Unsupported Unit"

def validate_and_execute(days_and_unit_dictionary):
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

user_input_message = "Hey USER, enter number of days & conversion unit!\n"