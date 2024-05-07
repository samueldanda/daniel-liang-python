# Prompt user to enter weight and price for package 1
weight_of_package_1, price_of_package_1 = eval(input("Enter weight and price for package 1: "))

# Prompt user to enter weight and price for package 2
weight_of_package_2, price_of_package_2 = eval(input("Enter weight and price for package 2: "))

# Calculating the price per unit weight for each package
price_per_unit_weight1 = price_of_package_1 / weight_of_package_1
price_per_unit_weight2 = price_of_package_2 / weight_of_package_2

print("Price per unit of package 1:", price_per_unit_weight1, "Price per unit of package 2:", price_per_unit_weight2)

if price_per_unit_weight1 < price_per_unit_weight2:
    print("Package 1 has better price.")
elif price_per_unit_weight2 < price_per_unit_weight1:
    print("Package 2 has better price.")
else:
    print("Both packages have the same price")
