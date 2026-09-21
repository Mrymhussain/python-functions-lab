# Exercise 1: Calculate Area of a Triangle

def calculate_area_triangle(base, height):
    return (base * height) / 2


print('Exercise 1:', calculate_area_triangle(10, 5))

# Exercise 2: Calculate Simple Interest

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


print('Exercise 2:', simple_interest(1000, 5, 2))

# Exercise 3: Apply a Discount

def apply_discount(price, discount):
    return price - (price * discount / 100)


print('Exercise 3:', apply_discount(100, 25))

# Exercise 4: Convert Temperature

def convert_temperature(temperature, unit):
    if unit == 'C':
        return (temperature * 9 / 5) + 32
    elif unit == 'F':
        return (temperature - 32) * 5 / 9


print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N

def sum_to(n):
    total = 0

    for number in range(1, n + 1):
        total += number

    return total


print('Exercise 5:', sum_to(6))

# Exercise 6: Find the Largest Number

def largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print('Exercise 6:', largest(1, 2, 3))

# Exercise 7: Calculate a Tip
def calculate_tip(bill, tip_percentage):
    return (bill * tip_percentage) / 100 

print('Exercise 7:', calculate_tip(50, 20))