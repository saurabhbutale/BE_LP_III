def knapsack_dp(values, weights, capacity, n):
    # Create a 2D array to store the maximum value at each n and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# User input
print("Enter the number of items:")
n = int(input())

values = []
weights = []

print("Enter the values of the items:")
for i in range(n):
    values.append(int(input(f"Value of item {i+1}: ")))

print("Enter the weights of the items:")
for i in range(n):
    weights.append(int(input(f"Weight of item {i+1}: ")))

print("Enter the capacity of the knapsack:")
capacity = int(input())

# Solve the 0-1 Knapsack problem
max_value = knapsack_dp(values, weights, capacity, n)

# Output the maximum value that can be carried
print(f"The maximum value that can be carried in the knapsack is: {max_value}")
