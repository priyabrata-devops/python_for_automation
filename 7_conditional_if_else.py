calculation_to_units = 24 * 60 * 60 # => Global Scope Variable
name_of_unit = "seconds"

def days_to_unit(num_of_days): # => Define a Function Parameter, it wiuld be a single or multi parameter
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "You entered 0 value, Please enter a valid positive number"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        days_of_unit = days_to_unit(user_input_number)
        print(days_of_unit)
    else:
        print("Your input is not a number, Don't ruin my program")

user_input = input("Hey USER, enter a number of days & I'll convert it to seconds \n") # input() always returns a string

validate_and_execute()