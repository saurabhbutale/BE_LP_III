# Item class to store value, weight, and calculate value per unit weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

# Function to solve Fractional Knapsack problem
def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0  # Total value in the knapsack
    for item in items:
        if capacity >= item.weight:
            # If the item can fit in the knapsack, take it completely
            total_value += item.value
            capacity -= item.weight
        else:
            # If the item can't fit completely, take the fractional part
            total_value += item.ratio * capacity
            break  # Knapsack is full now
    return total_value

# User input
print("Enter the number of items:")
n = int(input())

items = []
print("Enter the values and weights of the items:")
for i in range(n):
    value = int(input(f"Value of item {i+1}: "))
    weight = int(input(f"Weight of item {i+1}: "))
    items.append(Item(value, weight))

print("Enter the capacity of the knapsack:")
capacity = int(input())

# Solve the Fractional Knapsack problem
max_value = fractional_knapsack(items, capacity)

# Output the maximum value that can be carried
print(f"The maximum value that can be carried in the knapsack is: {max_value:.2f}")
