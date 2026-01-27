#generate a python code that takes year as an input and return whether it is leap year or not
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#generate a python code that accepts centimeters as input and returns&prints its inches by accurate calculation
def cm_to_inches(cm):
    inches = cm / 2.54
    return inches
centimeters = float(input("Enter length in centimeters: "))
inches = cm_to_inches(centimeters)
print(f"{centimeters} centimeters is equal to {inches} inches.")