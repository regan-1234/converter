print("Welcome to the converter!")
print("Please select your category:")
print()

conversions_available = [(1, "km", "mi"),
                         (2, "mi", "km"),
                         (3, "kg", "lbs"),
                         (4, "lbs", "kg"),
                         (5, "F", "C"),
                         (6, "C", "F"),
                        ]
print(conversions_available)
print()
for conversion_number, from_unit, to_unit in conversions_available:
    print(f"{conversion_number}: {from_unit} -> {to_unit}")

print()
conversion = input("Enter the number of the conversion to use -->")
conversion_index = int(conversion) - 1

conversion_number, from_unit, to_unit = conversions_available[conversion_index]
print()
from_value = float(input(f"Enter the {from_unit} -->"))
print()

if conversion_number == 1:
    to_value = from_value * 0.62
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")
elif conversion_number == 2:
    to_value = from_value * 1.61
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")
elif conversion_number == 3:
    to_value = from_value * 0.45
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")
elif conversion_number == 4:
    to_value = from_value * 2.22
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")
elif conversion_number == 5:
    to_value = (from_value -32) / 1.8
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")
elif conversion_number == 6:
    to_value = (from_value * 1.8) + 32
    print(f"{from_value} {from_unit} -> {to_value} {to_unit}")