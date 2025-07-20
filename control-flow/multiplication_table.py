#for loop to iterate through the numbers 1 to 10
#Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1,11):
    print(f"{number} * {i} = {number * i}")