amount = 50

while amount > 0:
    print("Amount Due:", amount)
    coin = int(input("Insert Coin: "))
    if coin in (5, 10, 25):
        amount -= coin

print("Change Owed:", abs(amount))
