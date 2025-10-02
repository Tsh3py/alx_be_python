def safe_divide(numerator, denominator):
   
    try:
        # Attempt to convert arguments to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt to perform division
        result = num / den

        # Return successful result in the required format
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # Handle non-numeric input for numerator or denominator
        return "Error: Please enter numeric values only."
