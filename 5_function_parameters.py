calculation_to_units = 24 * 60 * 60 # => Global Scope Variable
name_of_unit = "seconds"

def days_to_unit(num_of_days, custom_message): # => Define a Function Parameter, it wiuld be a single or multi parameter
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}") 
    print(custom_message) # => num_of_days, custom_message = Local Variable in Function

def scope_check():
    print(name_of_unit) # => It'll execute, as it is a global variable
#    print(custom_message) # => It'll fail, as it is a local variable


days_to_unit(20, "All Good!")
