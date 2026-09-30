coins = list(map(int, input("Enter coin denominations: ").split()))
target = int(input("Enter target amount: "))

dp = [0] * (target + 1)
dp[0] = 1

for coin in coins:
    for amount in range(coin, target + 1):
        dp[amount] += dp[amount - coin]

print("Total number of ways to make", target, ":", dp[target])
