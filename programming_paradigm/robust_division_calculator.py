

def safe_divide(numerator, denominator):
    
    try:
        denominator < 0
    except:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    try:
        float(numerator), float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
    return numerator / denominator