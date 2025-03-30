# Program for time converting
convert_from = str(input("What do you want to be converted? (minutes, seconds, hours): ")).lower()
# Validation logic (works unexpectedly)
"""while convert_from != "seconds" or convert_from != "minutes" or convert_from != "hours":
    print("You should type in only 'seconds' or 'hours or 'minutes'.")
    convert_from = str(input("What do you want to be converted? (minutes, seconds, hours): ")).lower()
"""
convert_to = str(input("What to convert to? (minutes, seconds, hours): ")).lower()
"""while convert_to != "seconds" or convert_to != "minutes" or convert_to != "hours":
    print("You should type in only 'seconds' or 'hours or 'minutes'.")
    convert_to = str(input("What to convert to? (minutes, seconds, hours): ")).lower()   """

# Validation logic that ensures that we cannot convert the same units
while convert_from == convert_to:
    print(f"You can't convert {convert_from} to {convert_to}.")
    print("Please try again.")
    convert_to = str(input("What to convert to? (minutes, seconds, hours): ")).lower()

num = int(input("Enter the number: "))

def time_converter(convert_from, convert_to, value):
    if convert_from == "seconds" and convert_to == "hours":
        hours = value / 3600
        return f"The {value} seconds = {hours} hours"
    
    elif convert_from == "seconds" and convert_to == "minutes":
        minutes = value / 60
        return f"The {value} seconds = {minutes} minutes"
    
    elif convert_from == "minutes" and convert_to == "hours":
        hours = value / 60
        return f"The {value} minutes = {hours} hours"
    
    elif convert_from == "minutes" and convert_to == "seconds":
        seconds = value * 60
        return f"The {value} minutes = {seconds} seconds"
    
    elif convert_from == "hours" and convert_to == "minutes":
        minutes = value * 60
        return f"The {value} hours = {minutes} minutes"
    
    elif convert_from == "hours" and convert_to == "seconds":
        seconds = value * 3600
        return f"The {value} hours = {seconds} seconds"
    
    else:
        return "Oops, Got unexpected behavior! Probably you should have written 'hours', 'minutes', 'seconds' in your 1st two inputs"
    
print(time_converter(convert_from, convert_to, num))  