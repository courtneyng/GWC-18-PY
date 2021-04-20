ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
print("If you add all the numbers together the sum is:", sum(numList))
# sum = 0
# for x in range(0,9):
    # sum = sum + list[x]
product = 1
for x in range(0, 9):
    product = product * ages[x]
print("If you multiply all the numbers in the list the product is:", product)

total = 0
for age in ages:
    total += ages

average = total / len(ages)
print(average)
