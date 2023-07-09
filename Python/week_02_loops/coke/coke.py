accepted_coins = [25, 10, 5]

coke_price = 50

paid = 0

due = coke_price

while paid < coke_price:
    coin = int(input("Insert coin: "))

    if coin in accepted_coins:
        paid = paid + coin
        due = coke_price - paid
        if due > 0:
            print(f"Amount Due: {due}")
        else:
            print (f"Change Owed: {due * -1}")
    else:
        print(f"Amount Due: {due}")

