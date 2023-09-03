calculation_to_units = 24 * 60 * 60 # => Global Scope Variable
name_of_unit = "seconds"

def days_to_unit(num_of_days): # => Define a Function Parameter, it wiuld be a single or multi parameter
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)

        if user_input_number > 0:
            days_of_unit = days_to_unit(user_input_number)
            print(days_of_unit)
        
        elif user_input_number == 0:
            print("You entered 0 value, Please enter a valid positive number")
        else:
            print("You entered negative value, Please enter a valid positive number")
    
    except ValueError:
        print("Your input is not a number, Don't ruin my program")

user_input = ""
while user_input != "exit":
    user_input = input("Hey USER, enter a number of days & I'll convert it to seconds \n") # input() always returns a string
    
    print(type(user_input.split(", ")))
    print(user_input.split(", "))

    print(type(set(user_input.split(", "))))
    print(set(user_input.split(", ")))

    print(user_input.split(", "))
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()