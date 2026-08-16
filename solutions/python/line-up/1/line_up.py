def line_up(name, number):
    # Example output:
    # "Mary, you are the 1st customer we serve today. Thank you!"

    # Rules
    # Numbers ending in 1 (unless ending in 11) → "st"
    # Numbers ending in 2 (unless ending in 12) → "nd"
    # Numbers ending in 3 (unless ending in 13) → "rd"
    
    # The function should take the name and number input.
    # return a string that includes the name and the number with the appropriate ordinal suffix.
    suffix = None

    if number % 10 == 1 and number % 100 != 11:
        suffix = "st"
    elif number % 10 == 2 and number % 100 != 12:
        suffix = "nd"
    elif number % 10 == 3 and number % 100 != 13:
        suffix = "rd"
    else:
        suffix = "th"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"